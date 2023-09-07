#Write a shell script that performs regular backups of a directory and rotates old backup files, ensuring a specified number of backups are retained.

#!/bin/bash

# Source directory to be backed up
source_dir="/path/to/source"

# Backup destination directory
backup_dir="/path/to/backup"

# Number of backups to retain
num_backups=5

# Create a timestamp for the backup
timestamp=$(date +%Y%m%d%H%M%S)

# Backup the source directory using rsync
rsync -avz "$source_dir" "$backup_dir/backup_$timestamp"

# List all backups and sort them by modification time
backup_list=$(find "$backup_dir" -maxdepth 1 -type d -name 'backup_*' | sort)

# Calculate the number of backups exceeding the limit
num_exceeding_backups=$(( $(echo "$backup_list" | wc -l) - num_backups ))

# Remove the oldest backups exceeding the limit
if [ $num_exceeding_backups -gt 0 ]; then
    backups_to_remove=$(echo "$backup_list" | head -n $num_exceeding_backups)
    echo "Removing old backups:"
    echo "$backups_to_remove"
    rm -r $backups_to_remove
fi
