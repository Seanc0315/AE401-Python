# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:40:37 2020

@author: James
"""

d = {'apple':10, 'banana':20}

d['orange'] = 15

d['banana'] = 30

print(d['apple'])

for i in d.keys():
    print(i)

for j in d.values():
    print(j)
    
for k in d.items():
    print(k)