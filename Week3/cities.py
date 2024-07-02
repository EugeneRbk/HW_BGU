#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 18:47:51 2024

@author: eugene
"""

def main():
    try:
        
        TEXT_PATH = 'cities.txt'
        SAVE_PATH = 'filtered_cities.txt'
        
        lcity = opening(TEXT_PATH)
        print(lcity)
        minpop = int(input("Please enter minimal population of the cities u r looking for:\n"))
        #print(fltr(lcity, 100000))
        sfcity = sort(fltr(lcity, minpop))
        
        save_to_file(sfcity, SAVE_PATH)
        
    except FileNotFoundError:
        print('#Error#\nCheck if "cities.txt" is present in the directory.')
    except:
        print("Unexpected error, contact developer")
    
    
def sort(lst):
    
    sorted_list = sorted(lst, key=lambda x: x[0]) 
    
    return(sorted_list) 
    
    
def fltr(sample, prmtr):
    
    newdata = []
    
    for i in range(len(sample)):
        number = ""
        for line in sample[i]:
            if line.isdigit():
                number += line
        if int(number) > prmtr:
            newdata.append(sample[i])
    
    return newdata
            

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

    print('Filtered and sorted data was saved successfully to "filtered_cities.txt"')



if __name__ == "__main__":
    main()
