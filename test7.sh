#Develop a menu-driven shell script that allows the user to perform various system administration tasks, such as user management, disk usage checks, and service status checks

#!/bin/bash

while true; do
    clear
    echo "System Administration Menu"
    echo "-------------------------"
    echo "1. User Management"
    echo "2. Disk Usage Check"
    echo "3. Service Status Check"
    echo "4. Exit"

    read -p "Enter your choice (1/2/3/4): " choice

    case $choice in
        1)
            clear
            echo "User Management Menu"
            echo "---------------------"
            echo "1. Add User"
            echo "2. Delete User"
            echo "3. List Users"
            echo "4. Back to Main Menu"

            read -p "Enter your choice (1/2/3/4): " user_choice

            case $user_choice in
                1)
                    # Add User logic here
                    echo "Add User selected."
                    ;;
                2)
                    # Delete User logic here
                    echo "Delete User selected."
                    ;;
                3)
                    # List Users logic here
                    echo "List Users selected."
                    ;;
                4)
                    continue
                    ;;
                *)
                    echo "Invalid choice. Press Enter to continue."
                    read
                    ;;
            esac
            ;;

        2)
            # Disk Usage Check logic here
            echo "Disk Usage Check selected."
            ;;
        3)
            # Service Status Check logic here
            echo "Service Status Check selected."
            ;;
        4)
            clear
            echo "Exiting the script. Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Press Enter to continue."
            read
            ;;
    esac
done
