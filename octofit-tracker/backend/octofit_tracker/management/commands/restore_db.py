import os
import glob
from django.core.management.base import BaseCommand
from django.conf import settings
import psycopg2
import psycopg2.extensions

class Command(BaseCommand):
    help = 'Restore PostgreSQL database from backup'

    def add_arguments(self, parser):
        parser.add_argument(
            '--backup-file',
            help='Specific backup file to restore from'
        )

    def handle(self, *args, **kwargs):
        backup_file = kwargs.get('backup_file')
        if not backup_file:
            # Find latest backup file
            backup_dir = os.path.join(settings.BASE_DIR, 'backups')
            backup_files = glob.glob(os.path.join(backup_dir, 'backup_*.sql'))
            if not backup_files:
                self.stdout.write(
                    self.style.ERROR('No backup files found')
                )
                return
            backup_file = max(backup_files, key=os.path.getctime)

        if not os.path.exists(backup_file):
            self.stdout.write(
                self.style.ERROR(f'Backup file not found: {backup_file}')
            )
            return

        try:
            # Get database settings
            db_settings = settings.DATABASES['default']
            
            # Connect to postgres database to handle database recreation
            conn = psycopg2.connect(
                dbname='postgres',
                user=db_settings['USER'],
                password=db_settings['PASSWORD'],
                host=db_settings['HOST'],
                port=db_settings['PORT']
            )
            conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            cur = conn.cursor()

            # Drop and recreate database
            self.stdout.write('Dropping existing connections...')
            cur.execute(f"""
                SELECT pg_terminate_backend(pid)
                FROM pg_stat_activity 
                WHERE datname = %s;
            """, [db_settings['NAME']])

            self.stdout.write('Recreating database...')
            cur.execute(f'DROP DATABASE IF EXISTS "{db_settings["NAME"]}"')
            cur.execute(f'CREATE DATABASE "{db_settings["NAME"]}"')
            
            # Close connection to postgres database
            cur.close()
            conn.close()

            # Connect to the target database
            conn = psycopg2.connect(
                dbname=db_settings['NAME'],
                user=db_settings['USER'],
                password=db_settings['PASSWORD'],
                host=db_settings['HOST'],
                port=db_settings['PORT']
            )
            conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            cur = conn.cursor()

            # Execute the backup file in stages
            self.stdout.write('Restoring schema...')
            with open(backup_file, 'r') as f:
                content = f.read()
                
                # Split the content into different parts
                lines = content.split('\n')
                drops = []
                creates = []
                constraints = []
                data = []
                
                current_section = 'drops'
                for line in lines:
                    if line.startswith('DROP TABLE'):
                        drops.append(line)
                    elif line.startswith('CREATE TABLE'):
                        creates.append(line)
                        current_section = 'creates'
                    elif line.startswith('ALTER TABLE'):
                        constraints.append(line)
                    elif line.startswith('INSERT INTO'):
                        data.append(line)
                
                # Execute in correct order
                for drop in drops:
                    cur.execute(drop)
                
                for create in creates:
                    cur.execute(create)
                
                for constraint in constraints:
                    try:
                        cur.execute(constraint)
                    except psycopg2.Error as e:
                        # Skip if constraint already exists
                        if 'already exists' not in str(e):
                            raise e
                
                for insert in data:
                    cur.execute(insert)

            cur.close()
            conn.close()

            self.stdout.write(
                self.style.SUCCESS(f'Successfully restored from {backup_file}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Restore failed: {str(e)}')
            )