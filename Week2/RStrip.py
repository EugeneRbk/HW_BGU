#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:12:00 2024

@author: eugene
"""

def main():
    
    TEXT_PATH = 'input.txt'
    SAVE_PATH = 'output.txt'
    
    try:
    
        ldata = opening(TEXT_PATH)
        
        print("Here is the current data in the text file:")
        
        for i in range(len(ldata)):
            print (ldata[i])
        
        todel = input("What symbols would u like to remove from right side.\n*Note. EOL symbol has already been deleted\nType in here: ")
        
        #print(delete(ldata, todel))
    
        #print(rev(ldata))
        
        save_to_file(rev(ldata), SAVE_PATH)

    except FileNotFoundError:
        print('#Error#\nCheck if "input.txt" is present in the directory.')
    except:
        print("Unexpected error, contact developer")

def rev(ltext):
    
    for i in range(len(ltext)):
        ltext[i] = ltext[i][::-1]
        
    return ltext


def delete(ltext, char):
    
    
    for i in range(len(ltext)):
        boof = ltext[i]
        
        for letter in char:
            ltext[i] = ltext[i].rstrip(char)
        
        if boof != ltext[i]:
            ltext[i] += ";"
            

    return ltext



def opening(path):
    with open(path, 'r', encoding='UTF-8') as file:
        
        doc =  file.readlines()
        for i in range(len(doc)):
            doc[i] = doc[i].rstrip()
    return doc


def save_to_file(text, adress):
    
    save = ""
    
    for i in range(len(text)):
        save += text[i] + "\n"
    
    with open(adress, 'w', encoding='UTF-8') as file:
        
        file.write(save)

    print('Saved successfully to "output.txt"')




if __name__ == "__main__":
    main()
