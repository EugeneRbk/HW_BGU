#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 20:54:05 2024

@author: eugene
"""

def main():
    
    try:
    
        TEXT_PATH = '/home/eugene/Python/BGU/KOBA/HW/3/input.txt'
    
        file = opening(TEXT_PATH)
        
        print(f'All the students data:\n{file}')
        course = input("Which course would you like to filter by?\n")
        enrolled = (filtration(file, course))
    
    except FileNotFoundError:
        print('#Error#\nCheck if "cities.txt" is present in the directory.')
    except:
        print("Unexpected error, contact developer")
    
    
    print(f'Students enrolled in {course}:\n{enrolled}')

def filtration(students, prmtr):
    
    line = ""
    
    for pupil in range(len(students)):
        students[pupil] = students[pupil].split(":")
        if students[pupil][1].find(prmtr) != -1: 
            line += students[pupil][0] + "\n"
            
    return line
    
def opening(path):
    with open(path, 'r', encoding='UTF-8') as file:
        
        doc =  file.readlines()
        for i in range(len(doc)):
            doc[i] = doc[i].rstrip()
    
    return doc





if __name__ == "__main__":
    main()