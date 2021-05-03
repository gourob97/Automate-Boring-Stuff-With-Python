tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def maxlen(mylist):
    max=0
    for item in mylist:
        if max<len(item):
            max = len(item)
    return max

colmaxsize=[]
for i in range(len(tableData)):
    colmaxsize.append(maxlen(tableData[i]))



for i in range(len(tableData[0])):
    print(tableData[0][i].rjust(colmaxsize[0])+' '+tableData[1][i].rjust(colmaxsize[1])+' '+tableData[2][i].rjust(colmaxsize[2]))
