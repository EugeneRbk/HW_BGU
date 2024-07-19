#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:52:44 2024

@author: eugene
"""


def main():
    
    first = incheck("Программа посчитает НОД 2 чисел")
    second = incheck()
    
    nod = recr(first,second)
    
    print(f'НОД заданных чисел: {nod}')
    
    pass

def recr(one, two):
    
    if one == 0 and two == 0:
        return print("У двух нолей нет НОД")
    elif one == 0:
        return (two)
    elif two == 0:
        return (one)
        

    if one > two:
         mx = one
         mn = two
    else:
         mn = one
         mx = two
    
    ostat = mx % mn
    
    if ostat == 0: 
        return mn
    else:
        return recr(mn, ostat)


def incheck(greetings = ""):
    
    print(greetings)
    
    while True:
        num = input("Введите число: ")
        if num.lstrip("-").isdigit():
            number = int(num)
            if number < 0:
                return number * (-1)
            else:
                return number
        else:
            print ("Ваш ввод не подходит, попробйте что-нибудь другое...")
        



if __name__ == "__main__":
    main()