# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:00:18 2021

@author: xl
"""

Q=str(input("輸入月租費形式及通話時間為:")).split(",")
q=int(Q[0])
if q==186:
    m=int(Q[1])*0.09
    if m<=186:
        m=186
    elif 186<m<=186*2:
        m*=0.9
    elif m>186*2:
        m*=0.8
elif q==386:
    m=int(Q[1])*0.08
    if m<=386:
        m=386
    elif 386<m<=386*2:
        m*=0.8
    elif m>386*2:
        m*=0.7
elif q==586:
    m=int(Q[1])*0.07
    if m<=586:
        m=586
    elif 586<m<=586*2:
        m*=0.7
    elif m>586*2:
        m*=0.6
elif q==986:
    m=int(Q[1])*0.06
    if m<=986:
        m=986
    elif 986<m<=986*2:
        m*=0.6
    elif m>986*2:
        m*=0.5
print("通話費為:%.0f" %m)
