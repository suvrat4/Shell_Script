#Write a shell script to generate a report of top memory-consuming processes.
#!/bin/bash

# Function to display the top N memory-consuming processes
show_top_memory_processes() {
    # Check if the user provided a number of processes to display
    if [ $# -ne 1 ]; then
        echo "Usage: $0 <number_of_processes>"
        exit 1
    fi

    num_processes="$1"

    # Use 'ps' to list processes, sort by memory usage, and display the top N
    ps aux --sort=-%mem | head -n "$num_processes"
}

# Check if the user provided the number of top processes to display
if [ $# -ne 1 ]; then
    echo "Usage: $0 <number_of_processes>"
    exit 1
fi

num_top_processes="$1"

echo "Top $num_top_processes Memory-Consuming Processes:"
show_top_memory_processes "$num_top_processes"
