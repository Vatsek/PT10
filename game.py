candies = 200

def start_game():
    game_status = True
    return game_status

    
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
        
    