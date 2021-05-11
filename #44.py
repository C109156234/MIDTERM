# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:54:45 2021

@author: xl
"""

M=int(input())
D=int(input())
S=(M*2+D)%3
if S==0:
    print("普通")
elif S==1:
    print("吉")
elif S==2:
    print("大吉")