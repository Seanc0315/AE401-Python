# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:54:17 2020

@author: James
"""
import random
d = {}

while True:
    print("1=加入詞彙", "2=列出全部單字", "3=英翻中", "4=中翻英", "5=測驗成果", "6=離開系統")
    m = input("請輸入功能(1~6)")
    if m == '1':
        voc = input("請輸入單字:")
        dif = input("請輸入解釋:")
        d[voc] = dif
    elif m == '2':
        for k,v in d.items():
            print(k,v)
    elif m == '3':
        voc1 = input("請輸入想查詢的單字")
        if voc1 in d:
            print(d[voc1])
    elif m == '4':
        dif2 = input("請輸入想查詢的中文單字:")
        for k,v in d.items():
            if dif2 == v:
                print(k)
    elif m == '5':
        k,v = random.choice(list(d.items()))
        print(k)
        answer = input("請輸入解釋:")
        if answer == v:
            print("答對了")
        else:
            print("再接再厲")
    elif m == '6':
        break