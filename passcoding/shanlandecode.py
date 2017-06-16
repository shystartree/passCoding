#!/usr/bin/env python
#-*- coding: UTF-8 -*-
def shanlan(password):
    b = len(password)
    print 'b=%d'%b

    # 计算栅栏长度
    for x in range(2, 100):
        for y in range(2, 100):
            if x * y == b:
                break
        if x*y==b:
            break
    print x,y
    i = 0
    code1 = []
    code2 = []
    # 从密文中抠出字符进行还原
    for j in range(0,y):  # x行y列
        for i in range(0, x):
            code1.append(password[i * y + j])
    x, y = y, x
    for j in range(0,y):  # y行x列
        for i in range(0, x):
            code2.append(password[i * y + j])
    # 恢复原来格式中的空格，帮助阅读

    codeone=''
    codetwo=''
    for i in code1:
        codeone=codeone+i
    for i in code2:
        codetwo=codetwo+i
    print codeone
    print codetwo


shanlan('KIQLWTFCQGNSOO')