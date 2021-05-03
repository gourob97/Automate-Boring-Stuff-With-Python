#! /usr/bin/python3

#this program will add '*' and a space to each line

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
    lines[i]='* '+lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
