#SECTION - status.py

#NOTE - The status of the player and the monster and their attributes
player_status = {
    'alive': True,
    'health': 100,
    'strength': 10
}

monster_status = {
    'alive': True,
    'health': 120,
    'strength': 5
}

game_status = {#if game is active
    'active': True
}

def update_status(entity, stat, value):#will update specific stats for the player and monster
    if entity == 'player':
        player_status[stat] += value#will add the value to the stat
    elif entity == 'monster':
        monster_status[stat] += value#will add the value to the stat

def get_status(entity):
    if entity == 'player':
        return player_status#recieves status of the player
    elif entity == 'monster':
        return monster_status#recieves status of the monster
