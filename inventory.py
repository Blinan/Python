# inventory.py

stuff = {'rope':1, 'torch':6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    itemTotal = 0
    for k, v in inventory.items():
        print(v,k)
        itemTotal += v
    print('Total number of items:' + str(itemTotal))

def addToInventory(inventory, addeditems):
    for item in addeditems:
        if item in inventory:
            inventory[item] +=1
        else:
            inventory[item] = 1
    return inventory

displayInventory(stuff)
print('\n\n\n\n\n')

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] 
stuff = addToInventory(stuff, dragonLoot) 
displayInventory(stuff)
