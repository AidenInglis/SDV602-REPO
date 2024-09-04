# inventory.py 
inventory = {
    'health_potion': False# deault false as game starts without any item
}

def add_item(item):
    if item in inventory:
        inventory[item] = True

def has_item(item):
    return inventory.get(item, False)

def use_item(item):
    if has_item(item):
        if item == 'health_potion':
            return True
    return False
