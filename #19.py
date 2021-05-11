# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:03:57 2021

@author: xl
"""

g=int(input("組數為:"))
for i in range(1,g+1):
    s=input("第%d組:" %i).split(" ")
    t=int(s[0])*250+int(s[1])*175
print("第%d組應收費用為:%d" %(i,t))
