# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:25:09 2020

@author: James
"""

num = input("請輸入人數:")
mathList = []
stList = []
highest = 0
lowest = 100

for i in range(int(num)):
    student = input("請輸入人名:")
    stList.insert(0, student)
    score = int(input("請輸入成績:"))
    mathList.insert(0, score)
    avg = int(sum(mathList)/int(num))
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score

print(mathList)
print(stList)
print("平均是", avg, "分")
print("最高分是", highest, "分")
print("最低分是", lowest, "分")
