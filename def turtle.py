# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:31:18 2020

@author: James
"""

import turtle
sean = turtle.Turtle()

def draw_square(unit):
    for i in range(4):
        sean.forward(unit)
        sean.left(90)

draw_square(10)
    
    