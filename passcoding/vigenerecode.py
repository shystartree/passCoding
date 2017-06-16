#!/usr/bin/env python
#-*- coding: UTF-8 -*-
def decode(cipherText):
    '''解密'''
    cipher=cipherText   #将密文中转存储以便后面恢复其中的空格
    cipherText=cipherText.replace(' ','')
    cipherText=cipherText.replace('\n','')
    print cipherText
    upMark=0   #判断密文大小写标记
    if cipherText[0]>96:
        upMark=1
    cipherText=cipherText.lower()
    print cipherText
    length = findKeyLen(cipherText)  # 得到密钥长度
    print 'length:',length
    key = findKey(cipherText, length)  # 找到密钥
    keyStr = ''
    for k in key:
        keyStr += k
    print('the Key is:', keyStr)
    plainText = ''
    index = 0
    for ch in cipherText:
        c = chr((ord(ch) - ord(key[index % length])) % 26 + 97)
        plainText += c
        index += 1
    if upMark==1:     #如果传入的密文是大写的，那么在处理结束时将其恢复成大写输出
        plainText.upper()
    print plainText
    return plainText


def findKeyLen(cipherText):
    '''寻找密钥长度'''
    length = 1
    maxCount = 0
    for step in range(1,len(cipherText)):#假定密钥长度在1到10之间
        count = 0
        for i in range(0,len(cipherText)-step):
            for i in range(step, len(cipherText) - step):
                if cipherText[i] == cipherText[i + step]:
                    count+=1
        if count>maxCount:
            maxCount = count
            length = step
    return length


def findKey(text, length):
    '''找出密钥'''
    key = []
    # 定义字母表频率列表
    alphaRate =[0.08167,0.01492,0.02782,0.04253,0.12705,0.02228,0.02015,0.06094,0.06996,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.0009,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.0015,0.01974,0.00074]
    matrix = textToList(text, length)
    for i in range(length):
        w = [row[i] for row in matrix]  # 取出每组密文中的第i个
        # print('w:',w)
        li = countList(w)  # 统计w中a-z出现的频率
        powLi = []  # 算乘积

        for j in range(26):
            Sum = 0.0
            for k in range(26):
                Sum += alphaRate[k] * li[k]
            powLi.append(Sum)
            li = li[1:] + li[:1]  # 循环移位
        Abs = 0.01
        ch = ''
        print powLi
        min=['a',0.0]
        for j in range(len(powLi)):
            if abs(powLi[j] - 0.0687) < Abs:
                if abs(powLi[j]-0.0687)<abs(min[1]-0.0687):
                    min=[chr(j+97),powLi[i]]
        key.append(min[0])
    return key


def countList(lis):
    '''统计列表中a-z出现的频率'''
    li = []
    print 'lis:',lis
    alphabet = [chr(i) for i in range(97, 123)]
    for c in alphabet:
        count = 0
        for ch in lis:
            if ch == c:
                count += 1
        count=float(count)
        li.append(count/len(lis))
    print li
    return li


def textToList(text, length):
    '''按密钥长度将text分组'''
    textMatrix = []
    row = []
    index = 0
    for ch in text:
        row.append(ch)
        index += 1
        if index % length == 0:
            textMatrix.append(row)
            row = []
    return textMatrix


