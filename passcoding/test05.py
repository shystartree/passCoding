#!/usr/bin/env python
#-*- coding: utf_8 -*-

import random, string


def sort_key(_key):
    L = []
    for k in _key:
        L.append(ord(k))
    L.sort()
    i = 1
    D = dict()
    for k in L:
        D[chr(k)] = i
        i += 1
    return D


# 生成指定长度随机字符串
def random_char(length):
    return ''.join(random.sample(string.ascii_letters, length))


def cloTransport_encode(plaintext, key):
    if not key or not key.strip():
        print('no keys')

    # 去空格
    _key = key.replace(' ', '')
    _plaintext = plaintext.replace(' ', '')

     # key排序
    D = sort_key(_key)

     # 判断是否整除并自动填满
    len_key = len(_key)
    len_plaintext = len(_plaintext)
    if len_plaintext % len_key == 0:
        line = int(len_plaintext / len_key)
    else:
        line = int(len_plaintext / len_key) + 1
        _plaintext = _plaintext + random_char(len_key - (len_plaintext % len_key))

     # 构建空参照表
    P = []
    for i in range(line):
        L = []
        P.append(L)

     # 填充参照表
    i = 0
    for j in range(line):
        for k in range(len_key):
            P[j].append(_plaintext[i])
            i += 1

     # 构建密码表
    Q = []
    dct = {}
    count = 0
    for j in range(len_key):
        for i in range(line):
            Q.append(P[i][j])
        dct[D[_key[count]]] = Q
        Q = []
        count += 1

    L = list(dct.keys())
    L.sort()

     # 生成密文字符串
    pwd = []
    for k in L:
        pwd.extend(dct[k])
        pwd.append(' ')
    password = ''.join(pwd)
    password.strip()
    print(password)
    return password


def cloTransport_decode(plaintext, key):
    if not key or not key.strip():
        print('no keys')

    _key = key.replace(' ', '')
    _plaintext = plaintext.replace(' ', '')

     # key排序
    D = sort_key(_key)
    key_dic = sorted(D.items(), key=lambda d: d[1], reverse=False)  # 在python2中D.iteritems()

    len_key = len(_key)
    len_plaintext = len(_plaintext)
    row = int(len_plaintext / len_key)

     # 构建空参照表
    P = []
    for i in range(len_key):
        L = []
        P.append(L)

     # 填充参照表
    i = 0
    for j in range(len_key):
        for k in range(row):
            P[j].append(_plaintext[i])
            i += 1

    d = {}
    j = 0
    for k, v in key_dic:
        d[k] = P[j]
        j += 1

    L = []
    count = 0
    for k in _key:
        L.append(d[k])
        count += 1

    dct = {}
    Q = []
    count = 0
    for i in range(row):
        for j in range(len_key):
            Q.append(L[j][i])
        dct[_key[count]] = Q
        Q = []
        count += 1

    pwd = []
    i = 0
    for k in _key:
        pwd.extend(dct[k])
        i += 1
        if i >= row:
            break

    password = ''.join(pwd)
    return password
password='qoury inpho Tkool hbxva uwmtd cfseg erjez'
key='how are u'
print cloTransport_decode(password,key)