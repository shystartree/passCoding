#!/usr/bin/env python
#-*- coding: UTF-8 -*-

class Caesar(str):

    """An implementation of the Caesar cipher."""

    def encipher(self, shift):
        """Encipher input (plaintext) using the Caesar cipher and return it
           (ciphertext)."""
        ciphertext = []
        for p in self:
            if p.isalpha():
                ciphertext.append(chr((ord(p) - ord('Aa'[int(p.islower())]) +
                shift) % 26 + ord('Aa'[int(p.islower())])))
            else:
                ciphertext.append(p)

        return ciphertext


    def decipher(self):
        """Decipher input (ciphertext) using the Caesar cipher and return it
           (plaintext)."""

        shift=raw_input('please input shift number of caesar\n ')
        if shift=='':
            for i in range(1,26):
                print 'if shift=%d ,plaintext is:'%i
                a=self.encipher(-i)
                tmp = ''
                for k in a:
                    tmp += k
                a=tmp
                if i<25:
                    print tmp

        elif 0<int(shift)<26:
            a=self.encipher(-int(shift))
            tmp = ''
            for k in a:
                tmp += k
            a = tmp
        return a

print Caesar('HTRUZYJW').decipher()

