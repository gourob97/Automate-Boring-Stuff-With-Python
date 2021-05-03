allGuest ={
    'Alice':{'apple':5,'pretzels':12},
    'Bob':{'ham sandwiches':3, 'apple':2},
    'Carol':{'cups':3, 'apple pies':1}
}

def totalBrought(guest,item):
    numBrought = 0
    for k,v in guest.items():
        numBrought+=v.get(item,0)
    return numBrought

print('Number of things being brought: ')

while True:
    print("Enter an item")
    item=input()
    if item=='':
        break
    else:
        qty=totalBrought(allGuest,item)
        print(str(qty))
    