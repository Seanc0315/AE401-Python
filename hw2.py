# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:29:51 2020

@author: James
"""

mg = input("請輸入你的數學成績:")
eg = input("請輸入你的英文成績:")
mg = int(mg)
eg = int(eg)

if mg < 60 and eg < 60:
    print("要懲罰")
elif mg >= 90 and eg >= 90:
    print("有獎勵")
else:
    print("再加油")