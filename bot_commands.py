from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import game_XO

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{datetime.datetime.now().time()}')
  
async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    items = mess.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text.split()
    
    await update.message.reply_text(game_XO.showMatrix())
    await update.message.reply_text(int(mess[1]))
    await update.message.reply_text(game_XO.player(int(mess[1])))