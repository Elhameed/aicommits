#!/usr/bin/env bash

# Remove the aicommit alias
sed -i '/alias aicommit="aicommit"/d' ~/.bashrc

# Delete the aicommit script
sudo rm /usr/local/bin/aicommit

# Uninstall the required Python packages
pip uninstall -y openai

echo "aicommit has been uninstalled."

