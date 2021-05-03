def displayInventory(inv):
    total =0

    for k,v in inv.items():
        print(str(v),"",k)
        total+=v

    print('Total number of items: '+str(total))


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory:
            inventory[item]=1
        else:
            inventory[item]+=1
    return inventory


    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
