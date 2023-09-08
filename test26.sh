#Create a simple menu-driven shell script that presents the user with options (e.g., 1. View files, 2. Edit file, 3. Quit) and uses a while loop to repeatedly prompt the user for their choice until they choose to quit.

#!/bin/bash

while true; do
    # Display the menu options
    echo "Menu:"
    echo "1. View files"
    echo "2. Edit file"
    echo "3. Quit"

    # Prompt the user for their choice
    read -p "Enter your choice: " choice

    # Use a case statement to perform actions based on user's choice
    case $choice in
        1)
            echo "Viewing files..."
            # Add your code here for viewing files
            ;;
        2)
            echo "Editing file..."
            # Add your code here for editing files
            ;;
        3)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please select 1, 2, or 3."
            ;;
    esac
done
