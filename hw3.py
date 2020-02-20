# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:45:00 2020

@author: James
"""

import random

answer = random.randint(1,10)

while True:
    playeranswer = input("請輸入數字:")
    playeranswer = int(playeranswer)
    if playeranswer < answer:
        print("大一點")
    elif playeranswer > answer:
        print("小一點")
    elif playeranswer == answer:
        print("你答對了")
        break