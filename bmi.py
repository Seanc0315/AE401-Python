# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:40:24 2020

@author: James
"""

w = input("weight:")
h = input("height(meter):")
bmi = int(w)//float(h) ** 2
print("BMI:", bmi)
if bmi < 18.5:
    print("過輕")
elif bmi >= 18.5 and bmi <= 24:
    print("正常")
else:
    print("過重")