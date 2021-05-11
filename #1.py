# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:56:00 2021

@author: xl
"""

Q=str(input("輸入一個正整數數字:"))
n=len(Q)
A=[]
B=[]
for i in range(0,n):
    for j in range(i+1,n+1):
        A.append(Q[i:j])
for j in range(0,len(A)):
    isprime=True
    a=A[j]
    for k in range(int(a)-1,1,-1):
        if int(a)%k==0:
            isprime=False
            break
    if isprime==True and int(a)>0:
        B.append(int(a))
if B==[]:
    print("No prime found")
else:
    print(max(B))
