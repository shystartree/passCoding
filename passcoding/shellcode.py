import re

def decode(password):
    if re.search('/x',password):
        password=password.replace('/x','')
    if re.search(r'\\x',password):
        password=password.replace('\\x','')
    print password.decode("hex")

