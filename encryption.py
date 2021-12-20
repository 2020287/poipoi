# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:08:51 2021

@author: SELAB
"""

def encrypt(data,shift):
    i=0
    Encrypted=[]
    while i<len(data):
        if ord(data[i])>90:
            
             Encrypted.append(chr((ord(data[i])+shift)-90+64))
             i=i+1
        else:
             Encrypted.append(chr(ord(data[i])+shift))
             i=i+1
    j=''.join(Encrypted)
    print(j)
def decrypt(data,shift):
    i=0
    Encrypted=[]
    while i<len(data):
        if ord(data[i])>90:
            
             Encrypted.append(chr((ord(data[i])-shift)+(-90+64)))
             i=i+1
        else:
             Encrypted.append(chr(ord(data[i])-shift))
             i=i+1
    j=''.join(Encrypted)
    print(j)

encrypt("ABZ",1)