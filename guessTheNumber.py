#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 23:13:27 2021

@author: gourob
"""

import random

secretNumber=random.randint(1,20)
print("I am thinking a number between 1 and 20")

flag=0

for i in range(7):
  
    print("Take a guess")
    guess=int(input())
    if(guess==secretNumber):
        print('Good job! You guessed my number in '+str(i+1) + ' guesses')
        flag=1
        break
    elif guess>secretNumber:
        print('Your guess is to high')
    else:
        print('Your guess is too low')

if flag==0:
    print('My secret number was'+ str(secretNumber))
    
    
    
    