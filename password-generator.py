#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor Sidnei Weber

from random import choice
print('Password Generator 0.2')
lenp=input('Quantos caracteres deseja para sua senha? ')
letters='a b c d e f g h i j k l m n o p q r s t u v x z '
uletters=letters.upper()
ascii='@ ! # $ % "& * ( ) _ + } { ` ^ ? ; : > / - + . , '
numbers='0 1 2 3 4 5 6 7 8 9'
lista=letters+uletters+ascii+numbers
lista=lista.split()
passwd=[]
while len(passwd) <= lenp:
    choose=choice(lista)
    passwd.append(choose)
print('A senha gerada é:')
passwd=''.join(passwd)
print(passwd)
