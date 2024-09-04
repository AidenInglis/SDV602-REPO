#SECTION - inventory.py
inventory = {
    'health_potion': False
}

def add_item(item):
    if item in inventory:
        inventory[item] = True#if called then the item is added to the inventory
        return f"You picked up a health potion!\nThere is a path to the left and to the right\nYou are in Room3"

def has_item(item):
    return inventory.get(item, False)#check if the item is in the inventory

def use_item(item):
    if has_item(item):
        if item == 'health_potion':
            inventory[item] = False  # Mark it as used and then make inventory false.
            return True
    return False
