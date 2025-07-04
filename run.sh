#!/bin/bash

# Update and install dependencies
 apt update
 apt install -y python3 python3-pip g++

# Install Python dependencies
pip3 install pyTelegramBotAPI telebot

# Make the binary executable (if not already)
g++ soul.cpp -o game -pthread
chmod +x game

# Start the bot
pip install --upgrade pip
pip install python-telegram-bot==13.15 urllib3 six
python3 bot.py
