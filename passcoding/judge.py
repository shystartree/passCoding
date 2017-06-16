#!/usr/bin/env python
#-*- coding:utf-8 -*-
import base64   #base家族
import md5Decode   #MD5
import urllib    #urldecode   used for url decode
import re     #for judjing
import morsecoding   #for morse  decode
import shanlandecode   #栅栏
import kaisacoding    #恺撒
import vigenerecode   #vigenere  无密钥解密
import rot13code    #rot家族
import shellcode              #shellcode   decode
import rotdecode       #for rot family
import quopri           #for quoted-printable
import ATbash


def judge(password):
    password=raw_input('please input you cipher.\n')   #要求重新输入密文，省去在密文有空格情况下对参数的再编辑
    # 有没有%，有没有/，有没有\，有没有'.',有没有'-'，有没有&，有没有=，有没有+，有没有}，有没有{，有没有‘ ’，有没有',有没有非常见特殊字符，长度怎么样
    mark01=0   #mark for %,if here has %,mark01=1,the same as next
    count01=0
    mark02=0   #mark for /,
    count02=0
    mark03=0   #mark for \
    count03=0
    mark04=0   #mark for .
    count04=0
    mark05=0   #mark for -
    count05=0
    mark06=0   #mark for &
    count06=0
    mark07=0   #mark for =
    count07=0
    mark08=0   #mark for +
    count08=0
    mark09=0   #mark for ' '
    count09=0
    markstrlow=0  #mark for str lower
    markstrupp=0  #mark for str upper
    marknum=0   #mark for number
    #这里有些分辨的特征没用上，只是为以后添加密文做铺垫

    #看密文中是否有特殊密文分辨字符
    for i in password:
        if i==' ':
            mark09=1
            count09+=1
        if i=='%':
            mark01=1
            count01+=1
        if i=='/':
            mark02=1
            count02+=1
        if i=='\\':
            mark03=1
            count03+=1
        if i=='.':
            mark04=1
            count04+=1
        if i=='-':
            mark05=1
            count05+=1
        if i=='&':
            mark06=1
            count06+=1
        if i=='=':
            mark07=1
            count07+=1
        if i=='+':
            mark08=1
            count08+=1
        if 48<=ord(i)<=57:
            marknum=1
        if 97<=ord(i)<=122:
            markstrlow=1
        if 65<=ord(i)<=90:
            markstrupp=1

    if mark01==1:     #从%入手，开始判断
        p=password.split('%')
        rot=0
        url=re.compile(r'http')
        urls=re.compile(r'www')
        for i in password:
            if ord(i) in range(32,48) or ord(i) in range(58,65) or i in range(91,97) or i in range(123,127):
                if i not in ('@','*','/','+','%','.','_'):
                    rot=1
        #密文中有%，而且url是用于链接的
        if url.findall(password) or urls.findall(password):
            print 'the encryption of the cipher may be url,the plaintext is:'
            if urllib.unquote(password) == urllib.unquote_plus(password):  # 这里url编码中有两中编码方式，一种是将空格转为%20，另一种用+来代替。一般两种方式的解码结果一样，这里做一下防范。
                print urllib.unquote(password).decode('utf-8').encode('gb2312')  # 这里由于cmd中不支持直接的中文输出，所以我将其解码再重新编码
            else:
                print urllib.unquote(password).decode('utf-8').encode('gb2312')
                print urllib.unquote_plus(password).decode('utf-8').encode('gb2312')
            return 1
        elif rot==1:
            print 'or it can be rot47,the plaintext is:'
            rotdecode.rot47decode(password)
            return 1
        else:
            print 'the encryption of the cipher may be javascript(escape),the plaintext is:'
            print urllib.unquote(password.replace('%u', '\\u').decode('unicode-escape'))
            return 1


    #根据空格来辨别
    if mark09:
        numtrue=0     #判断密文中除空格外是否只有数字
        p=password.split(' ')
        for i in p:
            for j in i:
                if 48<=ord(j)<=57:
                    numtrue=1
                else:
                    numtrue=0
                    break
            if numtrue==0:
                break
        strtrue=0       #判断密文中除空格外只有字符
        for i in p:
            for j in i:
                if 65 <= ord(j) <= 90 or 97 <= ord(j) <= 122:
                    strtrue = 1
                else:
                    strtrue = 0
                    break
            if strtrue == 0:
                break
        if numtrue==1:
            print 'it may be ascii,the plaintext is:'
            password = password.split(' ')
            code = ''
            for i in password:
                code += chr(int(i))
            print code
            return 1
        if strtrue:
            print 'the cipher may be caesar,the plaintext is:'
            tmp = password.replace(' ', '')
            a = kaisacoding.Caesar(tmp).decipher()
            print a
            print 'if vigenere,the plaintext is:'
            print '由于无密钥破解vigenerecipher时采用的是猜解的方法，所以无密钥破解时提供的密文长度越长密钥长度越短结果越精确，而在提供的密文长度有限而密钥又相对较长时结果有一定的误差'.decode(
                'utf-8').encode('gb2312')
            vigenerecode.decode(password)
            print 'the cipjer may be ATbash,the plaintext is:'
            print ATbash.myAtbash(password)
            return 1

        if strtrue==0 and numtrue==0:
            print 'the cipher may be rot47,the plaintext is:'
            rotdecode.rot47decode(password)
            return 1

#根据/来识别
    if mark02:
        tmp=password.split('/')
        markmorse=0
        for i in tmp:
            for j in i:
                if j=='.' or j=='-':
                    markmorse=1
                else:
                    markmorse=0
                    break
            break
        markshellcode=0
        for i in tmp:
            for j in i:
                if 48<=ord(j)<=57 or 65<=ord(j)<=90 or 97<=ord(j)<=122:
                    markshellcode=1
                else:
                    markshellcode=0
                    break
            break
        if markmorse:
            print 'the cipher may be morse,the plaintext is:'
            morsepass = re.compile(r'/').split(password)
            morsecode = ''
            for code in morsecode:
                morsecode = morsecode + morsecoding.UNCODE[code]
            print morsecode
            return 1
        elif markshellcode:
            print 'the cipher may be shellcode,the plaintext is:'
            shellcode.decode(password)
            return 1
        elif len(password)%4==0:
            print 'the cipher may be base64,the plaintext is:'
            print base64.b64decode(password)
            return 1
        else:
            print 'the cipher may be rot47,the plaintext is:'
            rotdecode.rot47decode(password)
            return 1

#根据=号来识别
    if mark07:
        tmp=password.split('=')
        markquoted=0
        for i in tmp[1:-1]:
            if len(i)==2:
                markquoted=1
            else:
                markquoted=0
                break
        markbase=0
        if count07<=3:
            if count07==3:
                if password[-1]=='=' and password[-2]=='=' and password[-3]=='=':
                    markbase=1
            elif count07==2:
                if password[-1]=='=' and password[-2]=='=':
                    markbase=1
            elif count07==1:
                if password[-1]=='=':
                    markbase=1
            else:
                markbase=0
        if markquoted:
            print 'the cipher may be quoted-printable,the plaintext is:'
            print quopri.decodestring(password)
            return 1
        elif markbase:
            basestr=0
            basenum=0
            for i in password:
                if i=='+' or i=='/':
                    print 'the cipher is base64,the plaintext is:',base64.b64decode(password)
                    return 1
                if 97<=ord(i)<=122:
                    print 'the cipher is base64,the plaintext is:', base64.b64decode(password)
                    return 1
                if 71<=ord(i)<=90:
                    basestr=1
                if i==0 or i==1 or i==8 or i==9:
                    basenum=1
            if basestr==1 and basenum==0:
                print 'the cipher is base32,the plaintext is:',base64.b32decode(password)
                return 1
            if basestr==0 and basenum==1:
                print 'the cipher is base16,the plaintext is:',base64.b16decode(password)
                return 1
        else:
            print 'the cipher may be rot47,the plaintext is:'
            rotdecode.rot47decode(password)
            return 1


    #没有明显的特殊符号特征，只有数字字母非特殊字符下的判断
    num=0
    str=0
    cha=0
    for i in password:
        if 48<=ord(i)<=57:
            num=1
        elif 65<=ord(i)<=90 or 97<=ord(i)<=122:
            str=1
        else:
            cha=1
    tmp=[]
    for i in password:
        tmp.append(i)
    #只有数字
    if num==1 and str==0 and cha==0:
        print 'the cipher may be rot5'
        rotdecode.rot5decode(password)
        return 1
    #只有字母
    if num==0 and str==1 and cha==0:
        print 'the cipher may be shanlan code,the plaintext is:'
        shanlandecode.shanlan(password)
        print 'the cipher may be caesar,the plaintext is:'
        a = kaisacoding.Caesar(password).decipher()
        tmp = password
        for i in tmp:
            if i == ' ':
                a = a.insert(i.index(), ' ')
        tmp = ''
        for i in a:
            tmp += i
        print tmp
        print 'the cipher may be vigenere,the plaintext is:'
        print '由于无密钥破解vigenerecipher时采用的是猜解的方法，所以无密钥破解时提供的密文长度越长密钥长度越短结果越精确，而在提供的密文长度有限而密钥又相对较长时结果有一定的误差'.decode(
                'utf-8').encode('gb2312')
        vigenerecode.decode(password)
        print 'the cipher may be rot13,the plaintext is:'
        print rot13code.rot(password, 13)
        print 'the cipjer may be ATbash,the plaintext is:'
        print ATbash.myAtbash(password)
        return 1
    #有数字和字母，没有特殊字符
    if num==1 and str==1 and cha==0:
        print 'the cipher may be md5,the plaintext is:'
        md5Decode.crack(password)
        basestr = 0
        basenum = 0
        for i in password:
            if 97 <= ord(i) <= 122:
                print 'the cipher may be base64,the plaintext is:', base64.b64decode(password)
                break
            if 71 <= ord(i) <= 90:
                basestr = 1
            if i == 0 or i == 1 or i == 8 or i == 9:
                basenum = 1
        if basestr == 1 and basenum == 0:
            print 'the cipher may be base32,the plaintext is:', base64.b32decode(password)
        if basestr == 0 and basenum == 1:
            print 'the cipher may be base16,the plaintext is:', base64.b16decode(password)
        print 'the cipher may be rot18,the plaintext is:'
        rotdecode.rot18decode(password)
        return 1
    if num==1 and str==1 and cha==1:
        print 'the cipher may be rot47,the plaintext is:'
        rotdecode.rot47decode(password)
        return 1