# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:30:54 2020

@author: James
"""

scoreList = []
num = int(input("請輸入人數:"))

for i in range(num):
    name = input("請輸入人名:")
    score = int(input("請輸入成績:"))
    scoreList.append([name, score])
print("最高分是", max(scoreList, key=lambda x:x[1]))
print("最低分是", min(scoreList, key=lambda x:x[1]))
print(sorted(scoreList, key=lambda x:x[1]))
    