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
    global game_state  # Use global to modify the global game_state variable
    print(f"game_play received direction: '{direction}' with current game_state: '{game_state}'")  # Debug statement

    if game_state == 'Room5':
        print(f"Handling Room5 commands: {game_places[game_state]}")  # Debug print to show current place info
        
        if direction.lower() in ['yes', 'no']:
            next_state = game_places[game_state].get(direction.lower())
            if next_state:
                print(f"Transitioning from {game_state} to {next_state}")  # Debug statement
                game_state = next_state  # Update the game state
                print(f"New game_state: {game_state}")  # Confirm the state change
                return game_places[game_state]['Story']
            else:
                print("Invalid state transition.")  # Debug statement
                return "Invalid transition."
        else:
            return "Invalid input.\nPlease choose 'yes' or 'no'."
    
    if game_state == 'BossRoom':
        print(f"Handling Bossroom commands: {game_places[game_state]}")  # Debug print to show current place info
        
        if direction.lower() in ['yes', 'no']:
            next_state = game_places[game_state].get(direction.lower())
            if next_state:
                print(f"Transitioning from {game_state} to {next_state}")  # Debug statement
                game_state = next_state  # Update the game state
                print(f"New game_state: {game_state}")  # Confirm the state change
                return game_places[game_state]['Story']
            else:
                print("Invalid state transition.")  # Debug statement
                return "Invalid transition."
        else:
            return "Invalid input for BossRoom\nPlease choose 'yes' or 'no'."
    
    if game_state == 'TooLate':
        print(f"Handling TooLate commands: {game_places[game_state]}")  # Debug print to show current place info
        
        if direction.lower() in ['yes', 'no']:
            next_state = game_places[game_state].get(direction.lower())
            if next_state:
                print(f"Transitioning from {game_state} to {next_state}")  # Debug statement
                game_state = next_state  # Update the game state
                print(f"New game_state: {game_state}")  # Confirm the state change
                return game_places[game_state]['Story']
            else:
                print("Invalid state transition.")  # Debug statement
                return "Invalid transition."
        else:
            return "Invalid input for 'TooLate'.\nPlease choose 'yes' or 'no'."


    #this snippet i need to rewrire for the boss fight and heal and item and so on with the player and monster stats.
    if game_state == 'BossFight':
            print(f"Handling BossFight commands: {game_places[game_state]}")  # Debug print to show current place info
            
            if direction.lower() in ['attack', 'heal']:
                next_state = game_places[game_state].get(direction.lower())
                if next_state: 
                    print(f"Transitioning from {game_state} to {next_state}")  # Debug statement
                    game_state = next_state  # Update the game state
                    print(f"New game_state: {game_state}")  # Confirm the state change
                    return game_places[game_state]['Story']
                else:
                    print("Have not setup this code yet")  # Debug statement
                    return "Invalid Region, Location not finished development."
            else:
                return "Invalid input for 'BossFight'.\nPlease choose 'attack' or 'heal'."

    elif direction.lower() in ['left', 'right']:
        proposed_state = game_places[game_state].get(direction.lower(), '')
        print(f"Proposed state for direction '{direction}': {proposed_state}")  # Debug statement
        
        if proposed_state == '':
            return 'You cannot go that way.\n' + game_places[game_state]['Story']
        else:
            game_state = proposed_state
            print(f"Updated game_state to: {game_state}")  # Confirm the state change
            return game_places[game_state]['Story']

    else:
        return "Invalid direction.\nPlease choose 'left' or 'right'."
