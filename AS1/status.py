# status.py

player_status = {
    'health': 100,
    'attack_strength': 10
}

monster_status = {
    'alive': True,
    'health': 50
}

def update_status(entity, stat, value):
    """
    Update the status of an entity (player or monster).

    Args:
        entity (str): 'player' or 'monster'.
        stat (str): The status to update (e.g., 'health', 'attack_strength').
        value (int): The value to update the status with.
    """
    if entity == 'player':
        player_status[stat] += value
    elif entity == 'monster':
        monster_status[stat] += value

def get_status(entity):
    """
    Get the status of an entity (player or monster).

    Args:
        entity (str): 'player' or 'monster'.

    Returns:
        dict: The status of the specified entity.
    """
    if entity == 'player':
        return player_status
    elif entity == 'monster':
        return monster_status
