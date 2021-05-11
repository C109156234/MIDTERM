# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:49:11 2021

@author: xl
"""

t=input("檢測的字串(end結束):")
if t=="end":
    print("檢測結束")
else:
    t=list(t)
    a=input("檢測的單一字元:")
    b=t.count(a)
    print("字元%s出現的次數為:%d" %(a,b))