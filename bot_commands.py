from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import datetime
import game_XO
import read_data_from_file
import datetime
import game
import random
from random import randrange

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name} !')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hello - бот поприветствует тебя\n\
/help - показать список комманд\n\
/sum - введите sum/ + два числа через пробел для отображения их суммы \n\
/time - показать текущую дату и время\n\
/ny - показать сколько дней осталось до Нового Года)!\n\
/aphorism - показать случайный афоризм\n\
/abstract - показать фрагмент конспекта pyhon\n\
/game - начать игру в кофеты\n\
/stop - закончить игру в конфеты досрочно')

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
    
async def show_aphorism_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(read_data_from_file.read_random_data_from_file('aphorism.txt'))
    
async def show_abstract_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(read_data_from_file.read_random_data_from_file('abstract_py.txt'))




async def game_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global game_status
    game_status = True
    if game_status == True:
        await update.message.reply_text(f'На столе лежит 200 конфет. Два игрока делают ход друг после друга. Первый ход определяется жеребьёвкой.\n'
                                        'За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
        await update.message.reply_text(f'Игра началась.')
    if random.randint(0, 2) == 1:
        message = 'Я хожу первый\n'
        await update.message.reply_text(message)
        quantity = randrange(1,29)
        candies = game.move_cpu(quantity)
        message = f'Я взял {quantity} конфет(ы)\n'
        await update.message.reply_text(message)
        message = f'На столе {candies} конфет(а)(ы).'
        await update.message.reply_text(message)
    else:
        message = 'Ваш ход'
        await update.message.reply_text(message)            

async def game_stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global game_status
    game_status = False
    game.stop_game()
    await update.message.reply_text(f'Игра закончена')

async def message_processing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global game_status
    if game_status == True:    
        if update.message.text[0] != '/':
                # ход игрока
            try:
                quantity = int(update.message.text)
            except:
                await update.message.reply_text('Я не понял ваш ответ. Напишите цифрой, сколько вы берете конфет.')
                return
            if not 0 < quantity < 29:
                await update.message.reply_text('можно брать только от 1 до 28 конфет')
                return
            if game.check_count(quantity):
                await update.message.reply_text(f'Жадина) Нельзя взять больше конфет чем осталось.')
                return
            candies = game.move_player(quantity)
            if game.finish_game():
                await update.message.reply_text('Поздравляю вас, вы выиграли')
                game_status = False
                game.stop_game()
                return
            message = (f'На столе {candies} конфет(а)(ы).')
            await update.message.reply_text(message)
            # ход cpu
            if candies < 29:
                    quantity = candies
            else:
                quantity = randrange(1,29)
            candies = game.move_cpu(quantity)
            message = f'Я взял {quantity} конфет(ы)\n'
            await update.message.reply_text(message)
            message = f'На столе {candies} конфет(а)(ы).'
            await update.message.reply_text(message)
            if game.finish_game():
                message = f'Я выиграл) Не расстраивайся) в следующий раз точно повезет)'
                await update.message.reply_text(message)
                game_status = False
                game.stop_game()
                return
            message = 'Ваш ход'
            await update.message.reply_text(message)
            return