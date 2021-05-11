# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:30:27 2021

@author: xl
"""

##21
account={"123 456":"9000","456 789":"5000","789 888":"6000","336 558":"10000","775 666":"12000","566 221":"7000"}
Q=int(input("輸入查詢組數N為:"))
for i in range(Q):
    a=input("")
    print(account.get(a,"error"))