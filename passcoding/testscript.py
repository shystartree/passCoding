#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xiaoqin00 on 2017/4/4

# !/usr/bin/env python

# -*- coding:utf-8 -*-

import math


def isPrime(n):
    if n <= 1:
        return False

    for i in xrange(2, int(math.sqrt(n) + 1)):

        if n % i == 0:
            return False

    return True


def crack(n):
    for p in xrange(2, n):
        for q in xrange(p + 1, n):
            if p * q == n and isPrime(p) and isPrime(q):
                print "p and q is:",(p,q)
                return (p,q)
#爆破质数

def extGcd(a, b):
    if a < b:
        return extGcd(b, a)

    if b == 0:
        return a, 1, 0

    gcd, x, y = extGcd(b, a % b)

    return gcd, y, x - a / b * y

#扩展欧几里得算法

def getD(n, e):
    print "crack is:",crack(n)
    p,q = crack(n)

    fai = (p - 1) * (q - 1)

    gcd, x, y = extGcd(fai, e)

    while y < 0:
        y += fai

    return y


def decrypt(n, e, ciphertext):
    plaintext = []

    d = getD(n, e)

    for num in ciphertext:
        num = pow(num, d, n)

        plaintext.append(chr(num))

    return "".join(plaintext)


if __name__ == "__main__":
    # n = 2449
    #
    # e = 7
    #
    # ciphertext = [971,922,605,1446,1704,889,2090,605,1899,
    #
    #               1915,2088,1988,1235,1032,65,922,958,1988,
    #
    #               2144,591,1988,2270,2088,1032,65,958,2233]
    n=920139713

    e=19

    ciphertext = [
    704796792,
    752211152,
    274704164,
    18414022,
    368270835,
    483295235,
    263072905,
    459788476,
    483295235,
    459788476,
    663551792,
    475206804,
    459788476,
    428313374,
    475206804,
    459788476,
    425392137,
    704796792,
    458265677,
    341524652,
    483295235,
    534149509,
    425392137,
    428313374,
    425392137,
    341524652,
    458265677,
    263072905,
    483295235,
    828509797,
    341524652,
    425392137,
    475206804,
    428313374,
    483295235,
    475206804,
    459788476,
    306220148,]

    print n,e,ciphertext

    plaintext = decrypt(n, e, ciphertext)

    print plaintext