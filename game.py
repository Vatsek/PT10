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
                    i[2] = 200
                    i[3] = move
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



    
def stop_game():
    global candies
    candies = 200
    game_status = False
    return game_status

def move_player(quantity):
    global candies
    candies -= quantity
    return candies

def move_cpu(quantity):
    global candies
    candies -= quantity
    return candies

def finish_game():
    if candies == 0:
        return True

def check_count(count):
    global candies
    return count > candies
        
def log(update: Update, context: CallbackContext):
    file = open('db.csv', 'a', encoding='utf8')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id},{update.message.text}\n')
    file.close()
    
    

    
