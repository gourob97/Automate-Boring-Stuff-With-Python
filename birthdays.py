birthdays = {'Alice' : 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name(blank to quit)')
    name=input()
    if name=='':
        break
    if name in birthdays:
        print(birthdays[name]+ ' is the birthday of '+name)
    else:
        print('I don\'t have the birthday information for '+name)
        print('What\'s his/her birthday? ')
        bday = input()
        birthdays[name]=bday
        print('Database Updated!')