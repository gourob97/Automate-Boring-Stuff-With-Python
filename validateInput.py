while True:
    print('Enter your age: ')
    age=input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')


while True:
    print('Enter a password(letters and number): ')
    password = input()
    if password.isalnum():
        break
    print('Please enter a valid password.')