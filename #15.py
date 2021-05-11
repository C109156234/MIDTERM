# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:03:29 2021

@author: xl
"""

s=list(input("輸入一組四位數字為:"))
for i in range(len(s)):
    s[i]=str((int(s[i])+7)%10)
s[0],s[2]=s[2],s[0]
s[1],s[3]=s[3],s[1]
print("輸出加密後的數字為:"+"".join(s))
