#Develop a shell script that reads a configuration file containing database connection details and performs automated database backups and maintenance.
db_config.conf file
# Database connection details
DB_HOST="localhost"
DB_USER="username"
DB_PASS="password"
DB_NAME="database_name"
=======================

#!/bin/bash

# Read the configuration file
source db_config.conf

# Backup database to a timestamped SQL file
backup_file="backup_$(date +\%Y\%m\%d\%H\%M\%S).sql"
mysqldump -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" > "$backup_file"

# Check if the backup was successful
if [ $? -eq 0 ]; then
    echo "Backup completed successfully: $backup_file"
else
    echo "Backup failed."
    exit 1
fi

# Perform database maintenance tasks here (e.g., optimizing tables)

# Clean up old backups (retain the last 5 backups)
backup_dir="/path/to/backups"
num_backups_to_keep=5

# List all backup files and sort them by modification time
backup_list=$(find "$backup_dir" -type f -name 'backup_*.sql' | sort -r)

# Calculate the number of backups exceeding the limit
num_exceeding_backups=$(( $(echo "$backup_list" | wc -l) - num_backups_to_keep ))

# Remove the oldest backups exceeding the limit
if [ $num_exceeding_backups -gt 0 ]; then
    backups_to_remove=$(echo "$backup_list" | tail -n $num_exceeding_backups)
    echo "Removing old backups:"
    echo "$backups_to_remove"
    rm $backups_to_remove
fi
