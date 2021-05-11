# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:58:20 2021

@author: xl
"""

Q=int(input("請輸入階層值M:"))
M=1
N=1
while M<=Q:
    N+=1
    M*=N
print("超過M為%d的最小階層N值為:%d" %(Q,N))
