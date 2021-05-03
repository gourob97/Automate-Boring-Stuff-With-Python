import copy

spam = ['A','B','C','D',[1,2,3]]
cheese = copy.deepcopy(spam)
cheese[1] = 'Hello'
print(cheese)
print(spam)