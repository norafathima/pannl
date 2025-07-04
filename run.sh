#!/bin/bash

# Update and install dependencies
apt update
apt install -y python3 python3-pip g++

# Install Python dependencies
pip3 install pyTelegramBotAPI

# Make the binary executable (if not already)
g++ soul.cpp -o game -pthread
chmod +x game

# Start the bot
pip install python-telegram-bot==13.15
python3 bot.py
