# command_parser.py

from story import game_play, show_current_place
from status import update_status

def parse_command(command):
    """
    Parse the player's command and execute the corresponding action.

    Args:
        command (str): The player's command.

    Returns:
        str: The result of the command (e.g., story text).
    """
    command = command.lower()
    
    if 'left' in command:
        return game_play('left')
    elif 'right' in command:
        return game_play('right')
    elif 'yes' in command:
        return game_play('yes')
    elif 'no' in command:
        return game_play('no')
    else:
        return "Invalid command. Please enter 'left', 'right', 'yes', or 'no'."
