#Develop a shell script that reads a configuration file containing oracle database connection details and performs automated database backups and maintenance for oracle
#!/bin/bash

# Function to perform database backup
perform_backup() {
    local db_user="$1"
    local db_password="$2"
    local db_sid="$3"
    local backup_dir="$4"
    local timestamp=$(date +"%Y%m%d%H%M%S")

    # Export data using expdp (replace with your preferred backup method)
    expdp "${db_user}/${db_password}@${db_sid}" directory=DATA_PUMP_DIR dumpfile=backup_${timestamp}.dmp

    # Perform RMAN backup (replace with your preferred backup method)
    rman target / <<EOF
    RUN {
        ALLOCATE CHANNEL c1 DEVICE TYPE DISK FORMAT '${backup_dir}/rman_%U.bkp';
        BACKUP DATABASE PLUS ARCHIVELOG;
        DELETE OBSOLETE;
    }
    EXIT;
    EOF
}

# Read configuration file
config_file="config.txt"

if [ ! -f "$config_file" ]; then
    echo "Error: Configuration file '$config_file' not found."
    exit 1
fi

while read -r line; do
    if [[ "$line" =~ ^\# ]]; then
        continue  # Skip comments in the config file
    fi

    IFS=':' read -r db_user db_password db_sid backup_dir <<< "$line"

    if [ -z "$db_user" ] || [ -z "$db_password" ] || [ -z "$db_sid" ] || [ -z "$backup_dir" ]; then
        echo "Error: Invalid configuration line in '$config_file'. Please check format."
        continue
    fi

    # Perform database backup and maintenance
    perform_backup "$db_user" "$db_password" "$db_sid" "$backup_dir"

done < "$config_file"
