#! /usr/bin/python3
#this is a simple and insecured [:p] password manager

# dictionary is choosen for password storage
passwords = {
    'gmail' : 'thisismygmailpassword',
    'facebook' : 'thisismyfacebookpassword',
    'twitter' : 'thisismytwitterpassword'
}

import sys
if len(sys.argv) < 2 :
    print('This program copies account password')
    sys.exit()
account = sys.argv[1]

import pyperclip

if account in passwords:
    pyperclip.copy(passwords[account])
    print("The password for "+account+ ' is copied to clipboard')
else:
    print("The is no password for "+account)
