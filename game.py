def game_start(id):
    game_progress.update({id: 0})
    # return game_progress[text][0]
    
def game_info(id):
    return game_progress[id]

def show_progress():
    return game_progress
    
def command():
    return

game_progress = {}
