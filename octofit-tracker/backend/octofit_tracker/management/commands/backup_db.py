from django.core.management.base import BaseCommand
from django.conf import settings
import os
import shutil
from datetime import datetime

class Command(BaseCommand):
    help = 'Backup SQLite database'

    def handle(self, *args, **kwargs):
        # Create backups directory if it doesn't exist
        backup_dir = os.path.join(settings.BASE_DIR, 'backups')
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Generate backup filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = os.path.join(backup_dir, f'backup_{timestamp}.sqlite3')

        try:
            # Copy the SQLite database file
            db_file = settings.DATABASES['default']['NAME']
            if os.path.exists(db_file):
                shutil.copy2(db_file, backup_file)
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created backup at {backup_file}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING('No database file found to backup')
                )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Backup failed: {str(e)}')
            )