#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 22:50:38 2021

@author: gourob
"""

# def spam(divideBy):
#     return 42/divideBy

def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

