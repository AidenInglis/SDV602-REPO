# command_parser.py
from story import game_play, get_game_state

def parse_command(command):
    command = command.lower().strip()
    current_state = get_game_state()
    print(f"Received command: '{command}' with current game_state: '{current_state}'")

    if current_state == 'Room5':
        print("Entered Room5 command handling")
        if 'yes' in command:
            return game_play('yes')
        elif 'no' in command:
            return game_play('no')
        else:
            return "You are in Room5\nInvalid command. Please enter 'yes' or 'no'."

    elif current_state == 'BossRoom':
        print("Entered BossRoom command handling")
        if 'yes' in command:
            return game_play('yes')
        elif 'no' in command:
            return game_play('no')
        else:
            return "You are in the BossRoom\nInvalid command. Please enter 'yes' or 'no'."

    elif current_state == 'TooLate':
            print("Entered TooLate command handling")
            if 'yes' in command:
                return game_play('yes')
            elif 'no' in command:
                return game_play('no')
            else:
                return "You are in the 'TooLate'\nInvalid command. Please enter 'yes' or 'no'."
            
    elif current_state == 'BossFight':
        print("Entered BossFight command handling")
        if 'attack' in command:
            return game_play('attack')
        elif 'heal' in command:
            return game_play('heal')
        else:
            return "You are in the BossFight\nInvalid command. Please enter 'attack' or 'heal'."


    else:
        if 'left' in command:
            return game_play('left')
        elif 'right' in command:
            return game_play('right')
        else:
            return "Invalid command. Please enter 'left' or 'right'."