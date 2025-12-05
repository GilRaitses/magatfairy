#!/bin/bash
# magatfairy.command - macOS double-clickable script
# Double-click this file to open Terminal and start conversion

# Get the directory where this script is located
cd "$(dirname "$0")"

# Run magatfairy with auto command
python3 magatfairy.py convert auto

# Keep terminal open so user can see results
echo ""
echo "Press any key to close..."
read -n 1

