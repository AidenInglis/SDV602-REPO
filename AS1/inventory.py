# inventory.py

player_inventory = []

def add_item(item):
    """Add an item to the player's inventory."""
    player_inventory.append(item)

def remove_item(item):
    """Remove an item from the player's inventory."""
    if item in player_inventory:
        player_inventory.remove(item)

def show_inventory():
    """Display the player's inventory."""
    return player_inventory
