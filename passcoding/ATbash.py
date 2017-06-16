#!/usr/bin/env python
#-*- coding: UTF-8 -*-

def myAtbash(encode_str):

	if not encode_str :
		return ''
	L = []
	for c in list(encode_str):
		if ord(c) == 32:
			L.append(c)
		elif ord(c)>= 65 and ord(c) <=90:
			c = chr( 155-ord(c) )
			L.append(c)
		elif ord(c) >= 97 and ord(c) <= 122:
			c = chr( 219-ord(c) )
			L.append(c)
		else:
			print('erro input')
			return ''
	return ''.join(L)

