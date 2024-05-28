#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 19:18:58 2024

@author: eugene
"""

def main():

    ones = ("", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать")
    
    tens = ("", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто")
    
    hunds = ("", "сто", "двесте", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот")
    
    
    num = incheck()
    otp = ""
    
    if 1 <= int(num) < 20:
        otp = (ones[int(num)])
        print (otp)
    
    elif int(num[1]) == 1 and int(num[2]) != 0:
        otp = (ones[int(num[1:])])
        print (hunds[int(num[0])], otp)    
    
    else:
        print (hunds[int(num[0])], tens[int(num[1])], ones[int(num[2])])


def incheck():

    while True:
        num = input("Введите число от 1 до 999:")
        if num.isdigit() and 1 <= int(num) <= 999 and len(num) < 4:
            return num
        else:
            print ("Ваш ввод не подходит, попробйте что-нибудь другое...")



if __name__ == "__main__":
    main()
    

    