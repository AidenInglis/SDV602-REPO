# story.py

game_state = 'Room1'

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
        'Image': 'assets/frog.png'
    },
    'Room4': {
        'Story': 'You are in Room4.\nthere is a path to the left.\nthere is a path to the right.',
        'left': 'Room5',
        'right': 'Room2',
        'Image': 'assets/forest_circle.png'
    },
    'Room5': {
        'Story': 'You are in Room5.\nThere are doors ahead of you, enter?',
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
        'Story': 'Did you forget that the door shut behind you?\n You are now trapped in the room with the Boss.\nPrepare to fight!\ntype ok to continue',
        'Image': 'assets/Boss.png'
    },
}

def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state
    return game_places[game_state]['Story']

# story.py

def game_play(direction):
    """
    Runs the gameplay based on direction

    Args:
        direction (str): Direction or action ('left', 'right', 'yes', 'no')

    Returns:
        str: The story at the current place
    """
    global game_state

    if game_state == 'Room5':
        if direction.lower() in ['yes', 'no']:
            game_state = game_places[game_state][direction.lower()]
            return game_places[game_state]['Story']
        else:
            return "Invalid input.\nPlease choose\n'yes' or 'no'."

    elif direction.lower() in ['left', 'right']:
        proposed_state = game_places[game_state].get(direction.lower(), '')
        if proposed_state == '':
            return 'You cannot go that way.\n' + game_places[game_state]['Story']
        else:
            game_state = proposed_state
            return game_places[game_state]['Story']
    else:
        return "Invalid direction.\n Please choose 'left' or 'right'."
