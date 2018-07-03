# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 09:56:03 2018

@author: DELL
"""
'''
题目001：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？ 
'''  
def tm001():  
    ''''' 
    【个人备注】：按题意直接写出来 
    '''  
    arr = []
    for i in range(1,5):
        for j in range(1,5):
            if j!=i:
                for k in range(1,5):
                    if k!=i and k!=j:
                        num = 100*i+10*j+k
                        arr.append(num)
    print(len(arr),arr)

def tm001_2():
    '''
    '''
    import itertools as it
    tempArr = list(it.permutations(range(1,5),3))
    arr = [100*t[0]+10*t[1]+t[2] for t in tempArr]
    print(len(arr),arr)
    
def tm002():
    I = eval(input("profit this month[10k]"))
    if 0<I<=10:
        bonus = I*0.1
    elif I<=20:
        bonus = 10*0.1+(I-10)*0.075
    elif I<=40:
        bonus = 10*0.1+10*0.075+(I-20)*0.05
    elif I<=60:
        bonus = 10*0.1+10*0.075+20*0.05+(I-40)*0.03
    elif I<=100:
        bonus = 10*0.1+10*0.075+20*0.05+20*0.03+(I-60)*0.015
    elif I>100:
        bonus = 10*0.1+10*0.075+20*0.05+20*0.03+40*0.015+(I-100)*0.01
    print("bonus should be:{:.2f}".format(bonus))

def tm002_2():
    I = int(input('profit(RMB)'))
    arrI = [1000000,600000,400000,200000,100000,0]
    rate = [0.01,0.015,0.03,0.05,0.075,0.1]
    bonus = 0
    for i in range(len(arrI)):
        if I>arrI[i]:
            bonus += (I-arrI[i])*rate[i]
            I = arrI[i]
    print(bonus)
    