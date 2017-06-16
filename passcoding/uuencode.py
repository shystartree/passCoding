#!/usr/bin/env python
#-*- coding:UTF-8 -*-
def uuencode(password):
    length = len(password)
    strmod = length % 3
    # 将如果密文不是3的倍数，就用null补成最近的3的倍数

    passbin=''
    for i in password:
        tmp=str(bin(ord(i)))
        tmp=tmp[2:]
        for j in range(8-len(tmp)):
            tmp='0'+tmp
        passbin=passbin+tmp
    for i in range(3 - strmod):
        passbin += '00000000'

    #将字符串补成3的倍数，然后转换为二进制，接下来就是对二进制字符串六位切割并转换为uuencode

    i=0
    plaintext=''
    while i < len(passbin):  # 将前面转化的二进制字符串每六位取一次，然后根据xxencode的转换表转换为相应字符
        a = passbin[i:i + 6]
        plaintext += chr(int(a, 2)+32)
        i += 6

    tmpend=''
    for i in range(3-strmod):
        tmpend+='`'
    plaintext=plaintext[:-(3-strmod)]+tmpend

    xxmod = len(plaintext) / 60  # 如果得到的密文长度大于六十，那就在前面每排的前面加上一个h，每六十位一行输出，最后一行不加h
    xxtmp = []
    xx = ''
    count = 0
    for i in plaintext:
        xx += i
        count += 1
        if count % 60 == 0:
            xx = 'M' + xx
            xxtmp.append(xx)
            xx = ''
            continue
        if count ==(xxmod * 60+1):
            xx=chr(((len(plaintext)-xxmod*60)/4)*3+32)+xx
        if plaintext.index(i)==len(plaintext):
            xxtmp.append(xx)

    if xxmod > 0:
        for i in xxtmp:
            print i + '\n'
    else:
        print xxtmp

def uudecode(password):

    fp=open('passwd.txt','r')
    tmp=[]
    for line in fp.readlines():    #从文件中读取密文，去掉h后放入一个数组中
        line=line.strip()
        print line
        if len(line)==61:
            line=line[1:]
        print line
        for i in line:
            for j in base:
                if i==j:
                    tmp.append(base.index(j))
    print tmp
    print len(tmp)

    tmptwo=''
    for i in tmp:                  #将数组元素转换为二进制，补全到八位，然后根据ascii还原
        a=bin(i)[2:]
        while len(a)<6:
            a='0'+a
        tmptwo+=a
    print tmptwo
    print len(tmptwo)
    i=0
    tmpplain=''
    while i<len(tmptwo):
        tmpthree=tmptwo[i:i+8]
        print chr(int(tmpthree,2))
        tmpplain+=chr(int(tmpthree,2))
        i+=8
    for i in range(1,4):
        if tmpplain[-i]==0:
            tmpplain=tmpplain[:-1]
    print tmpplain

password='The quick brown fox jumps over the lazy dog'
uuencode(password)

