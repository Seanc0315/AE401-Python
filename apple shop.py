# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:35:22 2020

@author: James
"""

num = 0
price = 0
saleList = []
increaseList = []

while True:
    print("1=設定", "2=進貨", "3=出貨", "4=營業額統計", "5=庫存統計", "6=離開系統")
    m = input("請輸入功能(1~6)")
    if m == '1':
        num = int(input("請輸入蘋果數量:"))
        price = int(input("請輸入價錢:"))
        print("蘋果", num, "顆", "一顆", price, "元")
    elif m == '2':
        increase = int(input("請問進貨了幾顆蘋果:"))
        increaseList.append(increase)
        num += increase
        print("現在有", num, "顆")
    elif m == '3':
        sale = int(input("請問出貨了幾顆:"))
        saleList.append(sale)
        num -= sale
        print("現在剩", num, "顆")
        print("賺了", price*sale, "元")
    elif m == '4':
        print("出貨了", len(saleList), "次")
        print("共賺了", sum(saleList)*price, "元")
        for i in range(len(saleList)):
            print("第"+str(i+1)+"次賺了", saleList[i]*price, "元")
    elif m == '5':
        print("原有", num+sum(saleList)-sum(increaseList), "個")
        print("出貨了", sum(saleList), "個")
        print("進貨了", sum(increaseList), "個")
        print("現有", num, "個")
    elif m == '6':
        break
    