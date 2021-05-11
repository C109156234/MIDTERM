# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:59:16 2021

@author: xl
"""
su=["國文","英文","微積分","體育","程式設計"]
l1=[]
for i in range(len(su)):
    n=int(input("%s:" %su[i]))
    l1.append(n)
s=0
for i in range(len(l1)):
    s+=l1[i]
    a=s/len(l1)
b=l1.index(max(l1))
sm=l1.index(min(l1))
print("平均分數:%0.2f" %a)
print("最高分科目:"+str(su[b])+str(max(l1))+"分")
print("最低分科目:"+str(su[sm])+str(min(l1))+"分")