#SECTION - story.py

game_state = 'Room1'

def get_game_state():
    #NOTE - Returns the current game state.
    global game_state
    return game_state

def set_game_state(new_state):
    #NOTE - Sets the game state to the new state.
    global game_state
    game_state = new_state

#SECTION - Game Places and all of their options and stories
game_places = {
    'Room1': {
        'Story': 'You are in Room1.\nthere is a path to the left.\nthere is a path to the right.',
        'left': 'Room2',
        'right': 'Room3',
        'Image': 'assets/forest.png'
    },
    'Room2': {
        'Story': 'You are in Room2.\nthere is a path to the left.\nthere is a path to the right.',
        'left': 'Room3',
        'right': 'Room1',
        'Image': 'assets/forest_circle.png'
    },
    'Room3': {
        'Story': 'You are in Room3\nthere is a path to the left.\nthere is a path to the right.\nThere is a box on the ground want to pick it up?',
        'left': 'Room4',
        'right': 'Room2',
        'pickup': 'healing potion',
        'Image': 'assets/frog.png'
    },
    'Room4': {
        'Story': 'You are in Room4.\nthere is a path to the left.\nthere is a path to the right.',
        'left': 'Room5',
        'right': 'Room2',
        'Image': 'assets/forest_circle.png'
    },
    'Room5': {
        'Story': 'You are in Room5.\nThere are doors ahead of you,\n with rumbling coming from inside, enter?',
        'yes': 'BossRoom',
        'no': 'Room4',
        'Image': 'assets/forest_circle.png'
    },
    'BossRoom': {
        'Story': 'The Door Slams Behind You!\nA Roar echos in throughout the chamber.\nTime to face the Boss, are you ready?',
        'yes': 'BossFight',
        'no': 'TooLate',
        'Image': 'assets/Boss.png'
    },
    'TooLate': {
        'Story': 'Did you forget? The door shut behind you?\n You are now trapped in the room with the Boss.\nPrepare to fight!\ntype yes to continue',
        'yes': 'BossFight',
        'Image': 'assets/Boss.png'
    },
    'BossFight': {
        'Story': 'Your turn to attack!\nPress "attack" to attack the Boss \nor use "heal" to use your potion to heal yourself.',
        'Image': 'assets/Boss.png'
    },
    'Win': {
        'Story': 'You defeated the Boss!\nYou Win!',
        'Image': 'assets/Boss.png'
    },
    'Lose': {
        'Story': 'The Boss defeated you!\nYou Lose!',
        'Image': 'assets/Boss.png'
    }
}

def show_current_place():
    #NOTE - Shows current place in the game
    global game_state
    return game_places[game_state]['Story']


def game_play(direction):
    #NOTE - This function is used to move the player around the game world and handle the inputs results.
    global game_state

    #handling for these three rooms as they need a yes or no input
    if game_state in ['Room5', 'BossRoom', 'TooLate']:
        if direction.lower() in ['yes', 'no']:
            next_state = game_places[game_state].get(direction.lower())
            if next_state:
                game_state = next_state
                return game_places[game_state]['Story']
            else:
                return "Invalid transition."
        else:
            return "Invalid input.\nPlease choose 'yes' or 'no'."
    #handling for the boss fight room - attack or heal
    if game_state == 'BossFight':
        if direction.lower() in ['attack', 'heal']:
            #BossFight does not need anything here as it is not required to change game state.
            return "Handling BossFight commands."
        else:
            return "Invalid input for BossFight. Please choose 'attack' or 'heal'."

    #handling for the rest of the rooms (1, 2, 3, 4)
    elif direction.lower() in ['left', 'right']:
        #gets next room based on direction and assigned to proposed_state
        proposed_state = game_places[game_state].get(direction.lower(), '')
        if proposed_state:
            game_state = proposed_state #if correct then continue to next room
            return game_places[game_state]['Story']
        else:
            return 'You cannot go that way.\n' + game_places[game_state]['Story']
    else:
        return "Invalid direction.\nPlease choose 'left' or 'right'."
