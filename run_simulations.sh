#!/bin/bash

# Create a screen, run the command, and close the screen
run_in_screen() {
    screen_name=$1
    command=$2

    # Create a detached screen and run the command
    screen -dmS "$screen_name" bash -c "$command; exec bash"
}

# Example commands to run
command1="echo 'Running command 1'; sleep 5"
command2="echo 'Running command 2'; sleep 3"

# Run each command in a separate screen
run_in_screen "screen1" "$command1"
run_in_screen "screen2" "$command2"

echo "Commands executed in separate screens."
