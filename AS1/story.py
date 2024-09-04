# story.py

game_state = 'Room1'

def get_game_state():
    global game_state
    return game_state

def set_game_state(new_state):
    global game_state
    game_state = new_state


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
        'Story': 'You are in Room3\nthere is a path to the left.\nthere is a path to the right.',
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
        'Story': 'You are in Room5.\nThere are doors ahead of you with rumbling coming from inside, enter?',
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
        'Story': 'The Boss attacks!\nYour turn to attack!\nType "attack" to attack the Boss or use "heal" to use your potion to heal yourself.',
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

#to show the current place function
def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state
    return game_places[game_state]['Story']


def game_play(direction):
    global game_state

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

    if game_state == 'BossFight':
        if direction.lower() in ['attack', 'heal']:
            # This is just for debugging, actual combat handling is managed in `command_parser.py`
            return "Handling BossFight commands."
        else:
            return "Invalid input for BossFight. Please choose 'attack' or 'heal'."

    elif direction.lower() in ['left', 'right']:
        proposed_state = game_places[game_state].get(direction.lower(), '')
        if proposed_state:
            game_state = proposed_state
            return game_places[game_state]['Story']
        else:
            return 'You cannot go that way.\n' + game_places[game_state]['Story']
    else:
        return "Invalid direction.\nPlease choose 'left' or 'right'."
