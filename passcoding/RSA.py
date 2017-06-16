#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xiaoqin00 on 2017/4/8


import os
import sys


# 分解模数n
def moder(n):
    base = 2
    while base < n:
        if n % base == 0:
            return base, n/base
        base += 1


# 求欧拉函数f(n)
def getEuler(prime1, prime2):
    return (prime1-1)*(prime2-1)


# 求私钥
def getDkey(e, Eulervalue):
    k = 1
    while True:
        if (((Eulervalue * k) + 1) % e) == 0:
            return (Eulervalue * k + 1) / e
        k += 1


# 私钥求明文
def decrypt(c, d, n):
    return pow(c, d, n)


def usage():
    print '[+] usage: python RSAtool.py [e] [n] [filepath]'
    print '[+] example: python RSAtool.py 19 920139713 1.txt'


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'argument error'
        usage()
        sys.exit()
    elif (str(sys.argv[1]).isdigit() is False) or (str(sys.argv[2]).isdigit() is False):
        print 'e and n must be digital'
        usage()
        sys.exit()
    elif int(sys.argv[1]) < 3:
        print 'e >= 3'
        print usage()
        sys.exit()
    elif not os.path.isfile(sys.argv[3]):
        print 'file path is error'
        usage()
        sys.exit()
    else:
        character = []
        digital = []
        e = int(sys.argv[1])
        n = int(sys.argv[2])
        primes = moder(n)
        p = primes[0]
        q = primes[1]
        pkey = getDkey(e, getEuler(p, q))
        with open(sys.argv[3], 'r') as f:
            data = f.readlines()
        linecount = 1
        for line in data:
            if (line.strip()).isdigit() is False:
                print "The %s line '%s' is not digital" % (str(linecount), line.strip())
            elif decrypt(int(line.strip()), pkey, n) >0 and decrypt(int(line.strip()), pkey, n) < 256:
                character.append(chr(decrypt(int(line.strip()), pkey, n)))
            digital.append(str(decrypt(int(line.strip()), pkey, n)))
            linecount += 1
        if character != []:
            print 'Character :%s' % ''.join(character)
        print 'Digital :%s' % ' '.join(digital)
