#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 20:21:38 2024

@author: eugene
"""

def main():
    
    n = incheck()
    if n == 0:
        print("Число вариаций: 0")
    else:
        print(f'Число вариаций: {recounter(n)}')




def recounter(height):
    
    if height <= 1:
        return 1
    return recounter(height-1) + recounter(height-2)
        


def incheck():

    while True:
        num = input("Введите число ступенек: ")
        if num.isdigit():
            return int(num)
        else:
            print ("Ваш ввод не подходит, попробйте что-нибудь другое...")
            
            
            


if __name__ == "__main__":
    main()