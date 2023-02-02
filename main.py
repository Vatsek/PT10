from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from bot_commands import *
import emoji

app = ApplicationBuilder().token("5918976065:AAGbKQWe8gC0q-yc9YPqqmLiyN4Mk15prYc").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("ny", days_to_new_year_command))
app.add_handler(CommandHandler("aphorism", show_aphorism_command))
app.add_handler(CommandHandler("abstract", show_abstract_command))
app.add_handler(CommandHandler("game", game_start))

print(emoji.emojize(f'Привет :thumbs_up:'))

print('Server Start')

app.run_polling()