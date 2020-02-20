# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:58:31 2020

@author: James
"""

import turtle
import time

count = 0
sean = turtle.Turtle()
sean.color('cyan')
sean.shape('turtle')
canvas = turtle.Screen()
canvas.title('my windows')
canvas.bgcolor('black')
move = 30
sean.penup()

for i in range(20):
  sean.stamp()
  sean.forward(move)
  sean.right(36)
  time.sleep(1)
  move += 5
turtle.done()
