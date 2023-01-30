from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
import emoji
from calc import *

app = ApplicationBuilder().token("5918976065:AAGbKQWe8gC0q-yc9YPqqmLiyN4Mk15prYc").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("play", play_command))
app.add_handler(CommandHandler("calc", calc_command))

print(emoji.emojize(f'Привет :thumbs_up:'))

print('Server Start')

app.run_polling()