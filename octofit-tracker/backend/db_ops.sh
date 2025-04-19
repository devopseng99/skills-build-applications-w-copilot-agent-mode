#!/bin/bash

case "$1" in
    "backup")
        echo "Creating database backup..."
        python manage.py backup_db
        ;;
    "restore")
        if [ -n "$2" ]; then
            echo "Restoring database from specific backup: $2"
            python manage.py restore_db --backup-file="$2"
        else
            echo "Restoring database from latest backup..."
            python manage.py restore_db
        fi
        ;;
    *)
        echo "Usage:"
        echo "  ./db_ops.sh backup              # Create a new backup"
        echo "  ./db_ops.sh restore             # Restore from latest backup"
        echo "  ./db_ops.sh restore [filename]  # Restore from specific backup file"
        ;;
esac