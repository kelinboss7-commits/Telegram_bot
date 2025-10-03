from telegram.ext import Updater, CommandHandler
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8067027755:AAG9WtKJ7mPH71h7oDWlBHg73TDdhQJ-K7o")
OWNER_ID = int(os.environ.get("OWNER_ID", "8067027755"))

def start(update, context):
    user_id = update.effective_user.id
    if user_id == OWNER_ID:
        update.message.reply_text("Welcome back, Owner! You can use this bot.")
    else:
        update.message.reply_text("This bot can only be used by its owner. Access denied.")

if __name__ == "__main__":
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
