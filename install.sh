#!/usr/bin/env bash

# Install the required Python packages
pip3 install openai

# Find the script file in the repository
script_path=$(find $(pwd) -name "aicommit.py" | head -1)

if [ -z "$script_path" ]
  then
    echo "Script file not found. Please make sure the script is named 'aicommit.py' and is located in the repository."
    exit 1
fi

# Copy the script file to /usr/local/bin
sudo cp "$script_path" /usr/local/bin/aicommit

# Make the script executable
sudo chmod +x /usr/local/bin/aicommit

# Define the alias
alias aicommit="aicommit"

# Add the alias to the .bashrc file
echo "alias aicommit='aicommit'" >> ~/.bashrc

# Reload the .bashrc file
source ~/.bashrc

echo "Installation complete. You can now use the 'aicommit' command."
