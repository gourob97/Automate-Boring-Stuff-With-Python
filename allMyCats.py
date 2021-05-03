#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:27:13 2021

@author: gourob
"""

cats =[]

while True:
    print("Enter name of the cat: ")
    name= input()
    if name=='':
        break;
    cats.append(name)

for cat in cats:
    print(cat, end=" ")
    