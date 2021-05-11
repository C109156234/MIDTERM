# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:59:42 2021

@author: xl
"""

Q=str(input("輸入值為:")).split(",")
Q.sort()
q=sorted(Q,reverse=True)
a="".join(Q)
b="".join(q)
ans=int(b)-int(a)
print("最大值數列與最小值數列差值為:%d" %ans)
