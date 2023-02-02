from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import datetime
import game_XO
import read_data_from_file
import datetime
import game


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name} !')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hello - бот поприветствует тебя\n\
/help - показать список комманд\n\
/sum - введите sum/ + два числа через пробел для отображения их суммы \n\
/time - показать текущую дату и время\n\
/ny - показать сколько дней осталось до Нового Года)!\n\
/aphorism - показать случайный афоризм\n\
/abstract - показать фрагмент конспекта pyhon')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{datetime.datetime.today()}')
  
async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    items = mess.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')
    
async def days_to_new_year_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = datetime.datetime.today()
    new_year = datetime.datetime(2024,1,1)
    delta = new_year - now
    await update.message.reply_text('До нового года осталось: {} дня(ей)'.format(delta.days))

async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text.split()
    
    await update.message.reply_text(game_XO.showMatrix())
    await update.message.reply_text(int(mess[1]))
    await update.message.reply_text(game_XO.player(int(mess[1])))
    
async def show_aphorism_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(read_data_from_file.read_random_data_from_file('aphorism.txt'))
    
async def show_abstract_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(read_data_from_file.read_random_data_from_file('abstract_py.txt'))

async def game_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    item = mess.split()
    item[0] = str(update.message.chat_id)
    await update.message.reply_text(item[0])
    game.game_start(item[0])
    await update.message.reply_text(game.game_info(item[0]))
    await update.message.reply_text(game.show_progress())
