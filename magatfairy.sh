#!/bin/bash
# magatfairy - Clickable script for macOS/Linux
# Double-click this file or run from terminal to start conversion

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Open terminal and run magatfairy with auto command
# On macOS, use Terminal.app; on Linux, use gnome-terminal or xterm
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    osascript -e "tell application \"Terminal\" to do script \"cd '$SCRIPT_DIR' && python3 magatfairy.py convert auto\""
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux - try gnome-terminal first, then xterm
    if command -v gnome-terminal &> /dev/null; then
        gnome-terminal -- bash -c "cd '$SCRIPT_DIR' && python3 magatfairy.py convert auto; exec bash"
    elif command -v xterm &> /dev/null; then
        xterm -e "cd '$SCRIPT_DIR' && python3 magatfairy.py convert auto; bash"
    else
        echo "Please run: cd '$SCRIPT_DIR' && python3 magatfairy.py convert auto"
    fi
else
    echo "Unsupported OS. Please run: cd '$SCRIPT_DIR' && python3 magatfairy.py convert auto"
fi

