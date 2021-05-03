#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:47:38 2021

@author: gourob
"""

def collatz(number):
    try:
        if number%2==0:
            return number//2
        else:
            return 3*number+1
    except:
        print("You must enter an integer")
        

while True:
    print("Enter a number")
    num=input()
    res = collatz(num)
    print(res)
    if res==1:
        break