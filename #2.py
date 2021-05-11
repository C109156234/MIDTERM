# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:56:42 2021

@author: xl
"""
##2
Q=int(input("輸入一個度數:"))
s=0
n=0
for i in range(1,Q+1):
    if i<=120:
        s+=2.10
        n+=2.10
    elif 120<i<=330:
        s+=3.02
        n+=2.68
    elif 330<i<=500:
        s+=4.39
        n+=3.61
    elif 500<i<=700:
        s+=4.97
        n+=4.01
    elif i>700:
        s+=5.63
        n+=4.50
print("Summer months:%0.2f" %(s))
print("Non-Summer months:%0.2f" %(n))
