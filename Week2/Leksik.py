#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 17:14:47 2024

@author: eugene
"""

def main():
    
    TEXT1_PATH = '/home/eugene/Python/BGU/KOBA/HW/2/input1.txt'
    TEXT2_PATH = '/home/eugene/Python/BGU/KOBA/HW/2/input2.txt'
    SAVE_PATH = '/home/eugene/Python/BGU/KOBA/HW/2/output.txt'
    
    try:
        
        ltext1 = opening(TEXT1_PATH)
        ltext2 = opening(TEXT2_PATH)
        
        print(analysis(ltext1,ltext2))
        save_to_file(analysis(ltext1,ltext2),SAVE_PATH)

    except FileNotFoundError:
        print('#Error#\nCheck if "input.txt" is present in the directory.')
    except:
        print("Unexpected error, contact developer")

    
def analysis(ltext1, ltext2):
    
    joined = []
    
    if len(ltext1) >= len(ltext2): # выбираем файл с большим количеством строк
        bigger = ltext1
        smaller = ltext2
    else:
        bigger = ltext2
        smaller = ltext1
        
    for i in range(len(bigger)): #идём по строкам
        
        try: # вдруг в одном файле больше строк, чем во втором
            
            if len(bigger[i]) >= len(smaller[i]): # сравниеваем с более короткой строкой
                
                for letter in bigger[i]: #идём по буквам в более короткой строке
                    
                    if bigger[i][::1] <= smaller[i][::1]:
                        joined.append(bigger[i] + smaller[i])
                        break
                    else:
                        joined.append(smaller[i] + bigger[i])
                        break
            else:
                for letter in bigger[i]: #идём по буквам в более короткой строке
                    
                    if bigger[i][::1] >= smaller[i][::1]:
                        joined.append(smaller[i] + bigger[i])
                        break
                    else:
                        joined.append(bigger[i] + smaller[i])
                        break
        
        except IndexError:
            joined.append(bigger[i])
    
                
    return joined
                


def opening(path):
    with open(path, 'r', encoding='UTF-8') as file:
        
        doc =  file.readlines()
        for i in range(len(doc)):
            doc[i] = doc[i].rstrip()
    return doc


def save_to_file(text, adress):
    pass
    save = ""
    
    for i in range(len(text)):
        save += text[i] + "\n"
    
    with open(adress, 'w', encoding='UTF-8') as file:
        
        file.write(save)

    print('Saved successfully to "output.txt"')

if __name__ == "__main__":
    main()