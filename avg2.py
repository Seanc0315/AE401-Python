# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:27:07 2020

@author: James
"""

scoreList = []
num = int(input("請輸入人數:"))

def input_data(): 
    for i in range(num):
        name = input("請輸入人名:")
        score = int(input("請輸入成績:"))
        scoreList.append([name, score])
       
def score_calculating():
    total = 0
    for k in range(num):
        total = total + scoreList[k][1]
    avg = total/num
    return avg

def highest_or_lowest():
    highest = 0
    lowest = 100
    lp = 0
    hp = 0
    for j in range(num):
        if scoreList[j][1] > highest:
            highest = scoreList[j][1]
            hp = scoreList[j][0]
    for g in range(num):
        if scoreList[g][1] < lowest:
            lowest = scoreList[g][1]
            lp = scoreList[g][0]
    print("最高分是", hp, highest, "分")
    print("最低分是", lp, lowest, "分")

input_data()
v = score_calculating()
highest_or_lowest()
print(v)
print(scoreList)