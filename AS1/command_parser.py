#SECTION - command_parser.py
from story import game_play, get_game_state
from monster_fight import MonsterFight
from inventory import add_item, has_item, use_item

monster_fight = MonsterFight()
def parse_command(command):#parses each command and executes code accordingly.
    command = command.lower().strip()#lower and strip each command.
    current_state = get_game_state()#set the current state

    if current_state == 'Room3':#if room three and pickup then call add_item to put in inventory
        if 'pickup' in command:
            add_item('health_potion')
            return add_item('health_potion')

    if current_state in ['Room5', 'BossRoom', 'TooLate']:
        return game_play(command)#handles the yes or no commands for the boss room and room 5.

    if current_state == 'BossFight':
        if command == 'attack':#if player attacking then...
            print("Debug: Player chose to attack")#for debugging
            result = monster_fight.player_attack()#player attack monster
            monster_action_result = monster_fight.monster_attack()#monster attack player
            return f"{result}\n{monster_action_result}"
        
        elif command == 'heal':#if heal then call the heal functionality for monster_fight.py
            print("Debug: Player chose to heal")
            if use_item('health_potion'):
                return monster_fight.player_heal()
            else:
                return "You don't have a health potion to use."
        else:
            return "Invalid command. Please enter 'attack' or 'heal'."

    if 'left' in command or 'right' in command:
        return game_play(command)#this handles the movement commands for left and right.
    else:
        return "Invalid command."