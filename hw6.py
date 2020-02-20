# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:53:13 2020

@author: James
"""

import random
r = random.randint(0,6)
r2 = random.randint(0,6)
r3 = random.randint(0,6)
sentenceList = []

for i in range(7):
    name = input("請輸入名字:")
    noun = input("請輸入名詞:")
    verb = input("請輸入動詞:")
    sentenceList.append([name, noun, verb])
print(sentenceList)
print(sentenceList[r][0], sentenceList[r2][2], sentenceList[r3][1])