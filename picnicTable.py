def printPicnic(itemDict, leftwidth, rightwidth):
    print('PICNIC ITEMS'.center(leftwidth+rightwidth,'-'))
    for k,v in itemDict.items():
        print(k.ljust(leftwidth,'.')+str(v).rjust(rightwidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
