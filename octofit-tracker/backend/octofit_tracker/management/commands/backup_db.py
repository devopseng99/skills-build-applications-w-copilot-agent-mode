import os
from datetime import datetime
from django.core.management.base import BaseCommand
from django.conf import settings
import psycopg2
import psycopg2.extensions

class Command(BaseCommand):
    help = 'Backup PostgreSQL database'

    def handle(self, *args, **kwargs):
        # Create backups directory if it doesn't exist
        backup_dir = os.path.join(settings.BASE_DIR, 'backups')
        os.makedirs(backup_dir, exist_ok=True)

        # Generate backup filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = os.path.join(backup_dir, f'backup_{timestamp}.sql')

        # Get database settings
        db_settings = settings.DATABASES['default']

        try:
            # Connect to the database
            conn = psycopg2.connect(
                dbname=db_settings['NAME'],
                user=db_settings['USER'],
                password=db_settings['PASSWORD'],
                host=db_settings['HOST'],
                port=db_settings['PORT']
            )
            conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

            # Create a cursor
            cur = conn.cursor()

            with open(backup_file, 'w') as f:
                # Write database schema
                f.write('-- Drop existing tables\n')
                cur.execute("""
                    SELECT 'DROP TABLE IF EXISTS "' || tablename || '" CASCADE;'
                    FROM pg_tables WHERE schemaname = 'public';
                """)
                for table in cur.fetchall():
                    f.write(f"{table[0]}\n")
                f.write('\n')

                # Get table creation commands
                cur.execute("""
                    SELECT table_name
                    FROM information_schema.tables 
                    WHERE table_schema = 'public'
                    ORDER BY table_name;
                """)
                tables = cur.fetchall()

                f.write('-- Create tables\n')
                for table in tables:
                    table_name = table[0]
                    
                    # Get column information
                    cur.execute("""
                        SELECT column_name, data_type, character_maximum_length, 
                               is_nullable, column_default
                        FROM information_schema.columns 
                        WHERE table_schema = 'public' AND table_name = %s
                        ORDER BY ordinal_position;
                    """, [table_name])
                    columns = cur.fetchall()

                    # Generate CREATE TABLE statement
                    column_defs = []
                    for col in columns:
                        name, dtype, max_length, nullable, default = col
                        col_def = f'"{name}" {dtype}'
                        if max_length:
                            col_def += f'({max_length})'
                        if default:
                            col_def += f' DEFAULT {default}'
                        if nullable == 'NO':
                            col_def += ' NOT NULL'
                        column_defs.append(col_def)

                    create_stmt = f'CREATE TABLE "{table_name}" ({" ".join(column_defs)});'
                    f.write(f"{create_stmt}\n")
                f.write('\n')

                f.write('-- Add constraints\n')
                for table in tables:
                    table_name = table[0]
                    # Get constraints
                    cur.execute("""
                        SELECT DISTINCT
                            tc.constraint_name, tc.constraint_type,
                            string_agg(kcu.column_name, ', '),
                            ccu.table_name AS foreign_table_name,
                            string_agg(ccu.column_name, ', ') AS foreign_column_name
                        FROM information_schema.table_constraints tc
                        LEFT JOIN information_schema.key_column_usage kcu
                            ON tc.constraint_name = kcu.constraint_name
                        LEFT JOIN information_schema.constraint_column_usage ccu
                            ON tc.constraint_name = ccu.constraint_name
                        WHERE tc.table_name = %s 
                        AND tc.constraint_type IN ('PRIMARY KEY', 'FOREIGN KEY', 'UNIQUE')
                        GROUP BY tc.constraint_name, tc.constraint_type, ccu.table_name;
                    """, [table_name])
                    
                    constraints = cur.fetchall()
                    for constraint in constraints:
                        name, type_, columns, ftable, fcolumns = constraint
                        if type_ == 'PRIMARY KEY':
                            f.write(f'ALTER TABLE "{table_name}" ADD PRIMARY KEY ({columns});\n')
                        elif type_ == 'FOREIGN KEY' and ftable:
                            f.write(f'ALTER TABLE "{table_name}" ADD CONSTRAINT "{name}" FOREIGN KEY ({columns}) REFERENCES "{ftable}" ({fcolumns});\n')
                        elif type_ == 'UNIQUE':
                            f.write(f'ALTER TABLE "{table_name}" ADD CONSTRAINT "{name}" UNIQUE ({columns});\n')
                f.write('\n')

                f.write('-- Insert data\n')
                for table in tables:
                    table_name = table[0]
                    # Get table data
                    cur.execute(f'SELECT * FROM "{table_name}";')
                    rows = cur.fetchall()
                    if rows:
                        columns = [desc[0] for desc in cur.description]
                        for row in rows:
                            values = [
                                'NULL' if val is None 
                                else f"'{str(val).replace("'", "''")}'"
                                for val in row
                            ]
                            f.write(
                                f'INSERT INTO "{table_name}" ("{", ".join(columns)}") '
                                f'VALUES ({", ".join(values)});\n'
                            )

            cur.close()
            conn.close()

            self.stdout.write(
                self.style.SUCCESS(f'Successfully backed up database to {backup_file}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Backup failed: {str(e)}')
            )