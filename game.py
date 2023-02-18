from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackContext

candies = 200
game_status = True

def start_game(update: Update, context: CallbackContext, move):
    players_status = read_data_from_file()
    player = update.effective_user.id
    with open('db.csv', 'w', encoding='utf8') as datafile:
        if len(players_status) != 0:
            for i in players_status:
                if str(player) in i:
                    i[2] = int(i[2])
                    i[2] = 200
                    i[3] = move
                else:
                    datafile.write(str(update.effective_user.id) + ',' + str(
                    update.effective_user.first_name) + ',' + '200' + ',' + str(move) + '\n')
            for j in players_status:
                for k in range(0, len(j)):
                    datafile.write(str(j[k]))
                    if k != len(j)-1:
                        datafile.write(',')
                datafile.write('\n')
        else:
            datafile.write(str(update.effective_user.id) + ',' + str(update.effective_user.first_name) + ',' + '200' + ',' + str(move) + '\n')
        
    return

def read_data_from_file():
    result = []
    with open('db.csv', 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result



    
def stop_game(update: Update):
    global candies
    candies = 200
    players_status = read_data_from_file() # получаем массив из файла
    player = update.effective_user.id
    with open('db.csv', 'w', encoding='utf8') as datafile:
        for i in players_status:
            if str(player) in i:
                i[2] = int(i[2])
                i[2] = 200
                candies = i[2]
        for j in players_status:
            for k in range(0, len(j)):
                datafile.write(str(j[k]))
                if k != len(j)-1:
                    datafile.write(',')
            datafile.write('\n')


    game_status = False
    return game_status



def move_player(update: Update, context: CallbackContext, quantity):
    global candies
    candies = 0
    players_status = read_data_from_file() # получаем массив из файла
    player = update.effective_user.id
    with open('db.csv', 'w', encoding='utf8') as datafile:
        for i in players_status:
            if str(player) in i:
                i[2] = int(i[2])
                i[2] -= quantity
                candies = i[2]
                i[3] = 1
        for j in players_status:
            for k in range(0, len(j)):
                datafile.write(str(j[k]))
                if k != len(j)-1:
                    datafile.write(',')
            datafile.write('\n')
    return candies

def move_cpu(update: Update, context: CallbackContext, quantity):
    global candies
    candies = 0
    players_status = read_data_from_file() # получаем массив из файла
    player = update.effective_user.id
    with open('db.csv', 'w', encoding='utf8') as datafile:
        for i in players_status:
            if str(player) in i:
                i[2] = int(i[2])
                i[2] -= quantity
                candies = i[2]
                i[3] = 0
        for j in players_status:
            for k in range(0, len(j)):
                datafile.write(str(j[k]))
                if k != len(j)-1:
                    datafile.write(',')
            datafile.write('\n')
    return candies

def finish_game():
    if candies == 0:
        return True

def check_count(update: Update, count):
    # global candies # потом удалить
    players_status = read_data_from_file() # получаем массив из файла
    player = update.effective_user.id
    with open('db.csv', 'w', encoding='utf8') as datafile:
        for i in players_status:
            if str(player) in i:
                i[2] = int(i[2])
                candies = i[2]
        for j in players_status:
            for k in range(0, len(j)):
                datafile.write(str(j[k]))
                if k != len(j)-1:
                    datafile.write(',')
            datafile.write('\n')
    return count > candies
        
# def log(update: Update, context: CallbackContext):
#     file = open('db.csv', 'a', encoding='utf8')
#     file.write(f'{update.effective_user.first_name},{update.effective_user.id},{update.message.text}\n')
#     file.close()
    
    

    
