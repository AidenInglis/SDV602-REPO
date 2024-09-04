# status.py

player_status = {
    'alive': True,
    'health': 100,
    'strength': 10
}

monster_status = {
    'alive': True,
    'health': 50,
    'strength': 5
}

game_status = {
    'active': True
}

def update_status(entity, stat, value):
    if entity == 'player':
        player_status[stat] += value
    elif entity == 'monster':
        monster_status[stat] += value

def get_status(entity):
    if entity == 'player':
        return player_status
    elif entity == 'monster':
        return monster_status
