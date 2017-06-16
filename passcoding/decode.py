#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys   #获取参数
import base64   #base家族
import getopt    #获取参数
import md5Decode   #MD5
import urllib    #urldecode   used for url decode
import re     #for judjing
import morsecoding   #for morse  decode
import shanlandecode   #栅栏
import kaisacoding    #恺撒
import vigenerecode   #vigenere  无密钥解密
import rot13code    #rot家族
from pycipher import Vigenere   #vigenere 有密钥解密
import shellcode              #shellcode   decode
import rotdecode       #for rot family
import quopri           #for quoted-printable
import judge     #判断密文
import ATbash     #埃特巴什
import xxencode   #xxencode
import cloTransport  #列位移

def usage():
    print("Usage:%s [-e encryptmethod] [--passwd=password] [--help]" % sys.argv[1])
    print 'encrypt methods can be base(base64|base32|base16)|md5|url|morse|javascript|shanlan|caesar|vigenere|' \
          'rot(rot5|rot13|rot18|rot47)|ascii|shellcode|quoted-printable|ATbash|xxencode'
    print "如果你的密文有'\n'分行，请将其保存在passwd.txt中"
mark=0
if __name__=='__main__':
    opts, args = getopt.getopt(sys.argv[1:], "e:", ["help", "passwd="])
    print opts

    def decode():
        try:
            for op, value in opts:
                if op == '--passwd':
                    password = value
                    print password

            for op, value in opts:
                if op == '--help':
                    usage()
                    sys.exit()
                elif op == '-e':
                    mark = 1  # mark对-e进行处理，如果没有加密方式参数就提交给自动判断加密方式函数处理
                    print value + ' decode:'
                    if value == 'base64':  # 对base家族的解码
                        print base64.b64decode(password)
                    elif value == 'base32':
                        password = password.replace("'", '')
                        print base64.b32decode(password)
                    elif value == 'base16':
                        password = password.replace("'", '')
                        print base64.b16decode(password)
                    elif value == 'md5':  # 对md5的解码，MD5解码过程中采用多线程查询多个网站数据库，防止出现单个网站查询不出数据的情况。
                        md5Decode.crack(password)
                    elif value == 'url':  # 对url编码的解码
                        if urllib.unquote(password) == urllib.unquote_plus(
                                password):  # 这里url编码中有两中编码方式，一种是将空格转为%20，另一种用+来代替。一般两种方式的解码结果一样，这里做一下防范。
                            print urllib.unquote(password).decode('utf-8').encode(
                                'gb2312')  # 这里由于cmd中不支持直接的中文输出，所以我将其解码再重新编码
                        else:
                            print urllib.unquote(password).decode('utf-8').encode('gb2312')
                            print urllib.unquote_plus(password).decode('utf-8').encode('gb2312')
                    elif value == 'morse':  # morse code 有两种格式一种间隔用空格表示，另一种则用/表示
                        password = password.strip("\'")
                        if re.search('/', password):  # /表示的morse解密
                            morsepass = re.compile(r'/').split(password)
                            morsecode = ''
                            for code in morsepass:
                                morsecode = morsecode + morsecoding.UNCODE[code]
                            print morsecode
                        elif args:  # 空格隔断的morse解密
                            code = morsecoding.UNCODE[password]
                            for i in args:
                                print i
                                code = code + morsecoding.UNCODE[i]
                            print code
                        else:  # 单个morse code decode
                            print morsecoding.UNCODE[password]
                    elif value == 'javascript' or value == 'escape':  # javascript解密
                        print urllib.unquote(password.replace('%u', '\\u').decode('unicode-escape'))
                    elif value == 'shanlan':
                        password = raw_input('please input your rail fence cipher again\n')  # 这里的再次输入为了防止长密文中出现空格的情况
                        shanlandecode.shanlan(password)
                    elif value == 'caesar':
                        password = raw_input('please input your password\n ')  # 防止出现空格而无法读取全部字符串的情况
                        password = password.replace(' ', '')
                        a = kaisacoding.Caesar(password).decipher()
                        print a
                    elif value == 'vigenere':
                        password = raw_input('please input your ciphertext\n')
                        key = raw_input('please input your key\n')
                        if key == '':
                            print '由于无密钥破解vigenerecipher时采用的是猜解的方法，所以无密钥破解时提供的密文长度越长密钥长度越短结果越精确，而在提供的密文长度有限而密钥又相对较长时结果有一定的误差'.decode(
                                'utf-8').encode('gb2312')
                            vigenerecode.decode(password)
                        else:
                            vig = Vigenere(key).decipher(password)
                            vigs = []
                            for i in vig:
                                vigs.append(i)
                            for i in range(0, len(password)):
                                if password[i] == ' ':
                                    vigs.insert(i, ' ')
                            vig = ''
                            for i in vigs:
                                vig += i
                            print 'the data after decode:%s\n' % vig
                    elif value == 'rot13':
                        print rot13code.rot(password, 13)
                    elif value == 'rot5':
                        rotdecode.rot5decode(password)
                    elif value == 'rot18':
                        rotdecode.rot18decode(password)
                    elif value == 'rot47':
                        rotdecode.rot47decode(password)
                    elif value == 'ascii':
                        password = raw_input('please input your cipher\n')
                        password = password.split(' ')
                        code = ''
                        for i in password:
                            code += chr(int(i))
                        print code
                    elif value == 'shellcode':
                        shellcode.decode(password)
                    elif value == 'quoted-printable':
                        a = quopri.decodestring(password)
                        print a.decode('utf-8').encode('gb2312')
                    elif value == 'ATbash':
                        password = raw_input('please input your cipher:\n')
                        print ATbash.myAtbash(password)
                    elif value == 'xxencode':
                        xxencode.xxdecode(password)
                    elif value == 'cloTransport':
                        password = raw_input('please input the passwd:')
                        key = raw_input('please input the key:')
                        cloTransport.cloTransport_decode(password, key)
                    elif value == 'base':  # base家族半模糊查询
                        basestr = 0
                        basenum = 0
                        for i in password:
                            if 97 <= ord(i) <= 122:
                                print 'the cipher may be base64,the plaintext is:', base64.b64decode(password)
                                exit()
                            if 71 <= ord(i) <= 90:
                                basestr = 1
                            if i == 0 or i == 1 or i == 8 or i == 9:
                                basenum = 1
                        if basestr == 1 and basenum == 0:
                            print 'the cipher may be base32,the plaintext is:', base64.b32decode(password)
                        if basestr == 0 and basenum == 1:
                            print 'the cipher may be base16,the plaintext is:', base64.b16decode(password)
                    elif value == 'rot':
                        mark = 0  # 判断密文中是否有特殊字符，有酒说明是rot47
                        marknotrot5 = 0  # 判断密文中是否有字母，有就说明不是rot5
                        marknotrot13 = 0  # 判断密文中是否有数字，有就说明不是rot13
                        for i in password:
                            if ord(i) < 48 or 57 < ord(i) < 97 or ord(i) > 122:
                                mark = 1
                            if 97 <= ord(i) <= 122:
                                marknotrot5 = 1
                            if 48 <= ord(i) <= 57:
                                marknotrot13 = 1
                        if mark == 1:
                            print 'rot47 decode:', rotdecode.rot47decode(password)
                        elif marknotrot5 == 0:  # 在确定密文中没有字母的情况下，可能是rot5，也可能是rot18，还可能使rot47
                            print 'str  is not in the password,it maybe rot5:', rotdecode.rot5decode(password)
                            print 'str is not in the password,it maybe rot18:', rotdecode.rot18decode(password)
                            print 'str is not in the password,it maybe rot47:', rotdecode.rot47decode(password)
                        elif marknotrot13 == 0:
                            print 'num is not in the password,it maybe rot13:', rot13code.rot(password, 13)
                            print 'num is not in the password,it maybe rot18:', rotdecode.rot18decode(password)
                            print 'num is not in the password,it maybe rot47:', rotdecode.rot47decode(password)
                        elif marknotrot13 == 1 and marknotrot5 == 1:
                            print 'rot18 decode:', rotdecode.rot18decode(password)
                    else:
                        print 'encrypt method error'
                        sys.exit()
                elif op != '--passwd':
                    print 'you should input your password you need to decode'
            if mark != 1:
                judge.judge(password)

        except getopt.GetoptError:
            print '参数获取失败'.decode('utf-8').encode('gb2312')
            sys.exit()




