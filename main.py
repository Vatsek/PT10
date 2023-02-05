from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from bot_commands import *
import emoji
import time
import game


app = ApplicationBuilder().token("token").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("ny", days_to_new_year_command))
app.add_handler(CommandHandler("aphorism", show_aphorism_command))
app.add_handler(CommandHandler("abstract", show_abstract_command))
app.add_handler(CommandHandler("stop", game_stop))
app.add_handler(CommandHandler("game", game_start))
app.add_handler(MessageHandler(None, message_processing))
print(emoji.emojize(f'Привет :thumbs_up:'))

print('Server Start')

app.run_polling()


