from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5918976065:AAGbKQWe8gC0q-yc9YPqqmLiyN4Mk15prYc").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum))

print('Server Start')

app.run_polling()