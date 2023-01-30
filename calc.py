from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import game_XO

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    number = update.message.text
    items = number.split()
    await update.message.reply_text(f'{int(items[1])} + 1')
    number2 = update.message.text
    items2 = number2.split()
    await update.message.reply_text(f'{int(items2[1])} + 1')
