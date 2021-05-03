#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 14:06:54 2021

@author: gourob
"""

n=int(input())
sum=0
for i in range(n+1):
    sum+=i
    
print(sum)


i=1
sum=0
while i<=n:
    sum+=i
    i+=1
    
print(sum)

