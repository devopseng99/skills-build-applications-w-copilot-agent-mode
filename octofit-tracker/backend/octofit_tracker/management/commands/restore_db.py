from django.core.management.base import BaseCommand
from django.conf import settings
import os
import shutil
import glob

class Command(BaseCommand):
    help = 'Restore SQLite database from backup'

    def add_arguments(self, parser):
        parser.add_argument(
            '--backup-file',
            type=str,
            help='Specific backup file to restore from. If not provided, will use most recent backup.'
        )

    def handle(self, *args, **kwargs):
        backup_dir = os.path.join(settings.BASE_DIR, 'backups')
        backup_file = kwargs.get('backup_file')

        if not backup_file:
            # Get the most recent backup file
            backup_files = glob.glob(os.path.join(backup_dir, 'backup_*.sqlite3'))
            if not backup_files:
                self.stdout.write(
                    self.style.ERROR('No backup files found!')
                )
                return
            backup_file = max(backup_files, key=os.path.getctime)
        elif not os.path.exists(backup_file):
            self.stdout.write(
                self.style.ERROR(f'Backup file {backup_file} does not exist!')
            )
            return

        try:
            # Get the database file path
            db_file = settings.DATABASES['default']['NAME']
            
            # Copy the backup file to the database location
            shutil.copy2(backup_file, db_file)
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully restored from {backup_file}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Restore failed: {str(e)}')
            )