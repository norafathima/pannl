#!/bin/bash

# Update and install dependencies
apt update
apt install -y python3 python3-pip g++

# Install Python dependencies
pip3 install pyTelegramBotAPI

# Make the binary executable (if not already)
chmod +x game

# Start the bot
python3 bot.py
