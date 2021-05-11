# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:00:26 2021

@author: xl
"""

s1=set(input("輸入s1為:"))
s2=set(input("輸入s2為:"))
if (s1<=s2):
    print("Yes")
else:
    print("No")
#---------------------------
s1=str(input("輸入s1為:"))
s2=str(input("輸入s2為:"))
if s1 in s2:
    print("Yes")
else:
    print("No")
