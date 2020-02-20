# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:46:33 2020

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

for i in range(10):
    sean.forward(100)
    sean.left(36)
    time.sleep(1)
turtle.done()