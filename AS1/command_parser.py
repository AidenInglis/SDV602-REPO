# command_parser.py
from story import game_play, get_game_state
from monster_fight import MonsterFight
from inventory import add_item, has_item, use_item

monster_fight = MonsterFight()
def parse_command(command):
    command = command.lower().strip()
    current_state = get_game_state()

    if current_state == 'Room3':
        if 'pickup' in command:
            add_item('health_potion')
            return "You picked up a health potion!"

    if current_state in ['Room5', 'BossRoom', 'TooLate']:
        return game_play(command)

    if current_state == 'BossFight':
        if command == 'attack':
            return monster_fight.player_attack()
        elif command == 'heal':
            if use_item('health_potion'):
                return monster_fight.player_heal()
            else:
                return "You don't have a health potion to use."
        else:
            return "Invalid command. Please enter 'attack' or 'heal'."

    if 'left' in command or 'right' in command:
        return game_play(command)
    else:
        return "Invalid command."
