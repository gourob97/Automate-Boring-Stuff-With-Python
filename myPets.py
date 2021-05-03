#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:38:14 2021

@author: gourob
"""

myPets =['Zophie', 'Pooka', 'Fat-tail']

print("enter a pet name")
name=input()

if name in myPets:
    print("I have the pet in my list")

if name not in myPets:
    print("I don't have the pet in my list")

