#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:44:53 2024

@author: eugene
"""



def main():
    
    h = incheck();
    
    width = 2*h - 1 # size of space
    
    empt = 0
    
    mid = int(width / 2)
    
    for i in range(h):
        
        for k in range(width):
            
            if (k <= mid + empt) and (k >= mid - empt):
                print ("*", end = "")
            
            else:
                print (" ", end = "")
    
        print ("")
        empt += 1 # increasing the width of "*"


def incheck():
    value = 0
    while value == 0:
        
        try:
            
            value = int(input("Please enter height of your triangle:\n"))
            if value < 0:
                value = value * (-1)
                print (f'\nSince your value is < 0, we took a module of it:) \n\nCurrent height: {value}\n')
            elif value == 0:
                print("\n#ERROR That's going to be an infinitely small trinagle, try something bigger:)\n")
                
        
        except:
            print("\n#ERROR Integer values only!\n")
            pass
        
    return value


if __name__ == "__main__":
    main()