# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:53:24 2020

@author: James
"""

import random

answer = random.randint(1,10)
count = 0

while True:
    if count == 5:
        print("你輸了")
        break
    playeranswer = input("請輸入數字:")
    count += 1
    playeranswer = int(playeranswer)
    if playeranswer < answer:
        print("大一點")
    elif playeranswer > answer:
        print("小一點")
    elif playeranswer == answer:
        print("你答對了")
        print("你猜了" + str(count) + "次")
        break
