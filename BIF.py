# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:11:46 2020

@author: James
"""

gradeList = [] #新增一個串列

for i in range(3): #重複三次指令
    g = int(input("請輸入成績:")) #輸入成績
    gradeList.append(g) #把資料存進串列
    
print(max(gradeList)) #印出串列的最大值
print(min(gradeList))
print(sorted(gradeList))
print(len(gradeList))
print(sum(gradeList))