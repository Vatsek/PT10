from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from bot_commands import *
import emoji

@bot.message_handler(commands=['game'])
def send_xo(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    one_one = types.KeyboardButton('1 1')
    one_two = types.KeyboardButton('1 2')
    one_tree = types.KeyboardButton('1 3')

    two_one = types.KeyboardButton('2 1')
    two_two = types.KeyboardButton('2 2')
    two_tree = types.KeyboardButton('2 3')

    tree_one = types.KeyboardButton('3 1')
    treee_two = types.KeyboardButton('3 2')
    tree_tree = types.KeyboardButton('3 3')
    markup.add(one_one, one_two, one_tree, two_one, two_two,
               two_tree, tree_one, treee_two, tree_tree)

    line_1 = ['..', '..', '..']
    line_2 = ['..', '..', '..']
    line_3 = ['..', '..', '..']
    all = [line_1, line_2, line_3]

    mess = f'|  {line_1[0]}  |  {line_1[1]}  |  {line_1[2]}  |\n|  {line_2[0]}  |  {line_2[1]}  |  {line_2[2]}  |\n|  {line_3[0]}  |  {line_3[1]}  |  {line_3[2]}  |\nвыберите позицию:'
    bot.send_message(message.chat.id, mess, reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def answer(message):
        # vinner = True

        Nolik = True
        black = True
        str = message.text.split()

        all = [line_1, line_2, line_3]
        while (black):
            if Nolik:
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                if all[x-1][y-1] == '..':
                    all[x-1][y-1] = 0
                    Nolik = False
                else:
                    x = random.randint(1, 3)
                    y = random.randint(1, 3)
                    if all[x-1][y-1] == '..':
                        all[x-1][y-1] = 0
                        Nolik = False
                    else:
                        x = random.randint(1, 3)
                        y = random.randint(1, 3)
                        all[x-1][y-1] = 0
                        Nolik = False

                black = True
            else:
                x = int(str[0])
                y = int(str[1])

                all[x-1][y-1] = 'X'
                mess = f'|  {line_1[0]}  |  {line_1[1]}  |  {line_1[2]}  |\n|  {line_2[0]}  |  {line_2[1]}  |  {line_2[2]}  |\n|  {line_3[0]}  |  {line_3[1]}  |  {line_3[2]}  |\nвыберите позицию:'
                bot.send_message(message.chat.id, mess, parse_mode='html')
                Nolik = True
                black = False

            if all[0][0] == 'X' and all[0][1] == 'X' and all[0][2] == 'X':
                bot.send_message(
                    message.chat.id, '/start x will winn ', parse_mode='html')
                break

            if all[1][0] == 'X' and all[1][1] == 'X' and all[1][2] == 'X':
                bot.send_message(
                    message.chat.id, '/start x will winn ', parse_mode='html')
                break
            if all[2][0] == 'X' and all[2][1] == 'X' and all[2][2] == 'X':
                bot.send_message(
                    message.chat.id, '/start \nx will winn ', parse_mode='html')
                break
            if all[0][0] == 'X' and all[1][1] == 'X' and all[2][2] == 'X':
                bot.send_message(
                    message.chat.id, '/start \nx will winn ', parse_mode='html')
                break
            if all[0][2] == 'X' and all[1][1] == 'X' and all[2][0] == 'X':
                bot.send_message(
                    message.chat.id, '/start \nx will winn ', parse_mode='html')
                break
            if all[0][0] == 'X' and all[1][0] == 'X' and all[2][0] == 'X':
                bot.send_message(
                    message.chat.id, '/start \nx will winn ', parse_mode='html')
                break
            if all[0][1] == 'X' and all[1][1] == 'X' and all[2][1] == 'X':
                bot.send_message(
                    message.chat.id, '/start \nx will winn ', parse_mode='html')
                break
            if all[0][2] == 'X' and all[1][2] == 'X' and all[2][2] == 'X':
                bot.send_message(
                    message.chat.id, '/start \nx will winn', parse_mode='html')
                break

            if all[0][0] == 0 and all[0][1] == 0 and all[0][2] == 0:
                bot.send_message(
                    message.chat.id, '/start \n0 will winn ', parse_mode='html')
                break
            if all[1][0] == 0 and all[1][1] == 0 and all[1][2] == 0:
                bot.send_message(
                    message.chat.id, '/start \n0 will winn ', parse_mode='html')
                break
            if all[2][0] == 0 and all[2][1] == 0 and all[2][2] == 0:
                bot.send_message(
                    message.chat.id, '/start \n0 will winn ', parse_mode='html')
                break
            if all[0][0] == 0 and all[1][1] == 0 and all[2][2] == 0:
                bot.send_message(
                    message.chat.id, '/start \n0 will winn ', parse_mode='html')
                break
            if all[0][2] == 0 and all[1][1] == 0 and all[2][0] == 0:
                bot.send_message(
                    message.chat.id, '/start \n0 will winn ', parse_mode='html')
                break
            if all[0][0] == 0 and all[1][0] == 0 and all[2][0] == 0:
                bot.send_message(
                    message.chat.id, '/start \n0 will winn ', parse_mode='html')
                break
            if all[0][1] == 0 and all[1][1] == 0 and all[2][1] == 0:
                bot.send_message(
                    message.chat.id, '/start \n0 will winn ', parse_mode='html')
                break
            if all[0][2] == 0 and all[1][2] == 0 and all[2][2] == 0:
                bot.send_message(
                    message.chat.id, '/start \n 0 will winn ', parse_mode='html')
                break

            if all[0].count('..') == 0 and all[1].count('..') == 0 and all[2].count('..') == 0:
                bot.send_message(
                    message.chat.id, '/start \nничья', parse_mode='html')
                break