import re
def rot5decode(password):
    plaintext=''
    for i in password:
        if ord(i)<=57:
            plaintext+=chr((int(i)+5)%10+48)
    print plaintext
def rot18decode(password):
    plaintext=''
    for i in password:
        if ord(i)<=57:
            plaintext += chr((int(i) + 5) % 10 + 48)
        elif 65<=ord(i)<=90:
            plaintext+=chr((ord(i)-65+13)%26+65)
        elif 97<=ord(i)<=122:
            plaintext+=chr((ord(i)-97+13)%26+97)
    print plaintext
def rot47decode(password):
    plaintext=''
    for i in password:
        plaintext+=chr((ord(i)-33+47)%94+33)
    print plaintext