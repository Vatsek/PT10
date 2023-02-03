from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from bot_commands import *
import emoji



async def message_processing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработка сырого текста в чате"""
    if update.message.text[0] != '/':
        if game.gamestatus:
            # запущена игра
            # ход игрока
            try:
                matches = int(update.message.text)
            except:
                await update.message.reply_text('Я не понял ваш ответ. Напишите цифрой, сколько вы берете спичек.')
                return
            if not 0 < matches < 9:
                await update.message.reply_text('можно брать только от 1 до 8 спичек')
                return
            game.action_player(matches)
            if game.check_game_state():
                await update.message.reply_text('Поздравляю вас, вы выиграли')
                game.stop()
                return
            message = f'На столе {game.heap} спичек.'
            await update.message.reply_text(message)
            sleep(1)
            # ход компьютера
            message = f'Я взял {game.action_cpu()} спичек\n'
            await update.message.reply_text(message)
            message = f'На столе {game.heap} спичек.'
            await update.message.reply_text(message)
            sleep(1)
            if game.check_game_state():
                message = f'Я выиграл'
                await update.message.reply_text(message)
                game.stop()
                return
            message = 'Ваш ход'
            await update.message.reply_text(message)
            return

app = ApplicationBuilder().token("5918976065:AAGbKQWe8gC0q-yc9YPqqmLiyN4Mk15prYc").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("ny", days_to_new_year_command))
app.add_handler(CommandHandler("aphorism", show_aphorism_command))
app.add_handler(CommandHandler("abstract", show_abstract_command))
app.add_handler(CommandHandler("game", game1))

print(emoji.emojize(f'Привет :thumbs_up:'))

print('Server Start')

app.run_polling()


