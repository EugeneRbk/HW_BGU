#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:36:56 2024

@author: eugene
"""

import random
import numpy as np

def main():
    
    n = 1
    animals = {}
    global POL 
    POL = "fm"
    plants = 1000
    
        
    print("EDITORS NOTE\n*Carnivoars can hunt only plant eating animals*")
    print("\nWelcome to biosystem, where you can create one and see how it goes\n\n\n")
    print_subclasses()
    print(f'Current plants: {plants}')
    
    
    while True:
        
        des = incheck("\n1 - Generating animals; 2 - Breeding animals; 3 - adding plants, 4 - next day\nEnter: ")
        if des == 1:
            notpresent = True
            while notpresent:
                whom = input("Please put in the name of the animal, that u want to add: ")
                hmany = incheck(f'How many {whom}(s) would you like to add:  ')
                try:
                    add_species(animals, whom, class_from_name(whom), hmany)
                    notpresent = False
                    print(f'\033[92m---{hmany} species of {whom} were successfully added to the system---\033[0m') # GREEN
                    print ("Current habitats:")
                    printout(animals)
                except:
                    print("\033[91m#ERROR\033[0m No such animal in the system, try another one.") #RED
        
        elif des == 2:
            whom = input("Please put in the name of the animal, that u want to breed: ")
            try:
                breeding(animals, whom)
                printout(animals)
            except:
                print("\033[91m#ERROR\033[0m No such animal in the system, try another one.")
                
        elif des == 3:
            added = incheck("How many plants would you like to add:  ")
            plants += added
            print(f'Current number of plants is: {plants}')
            
        elif des == 4:
            many = incheck("How many days them would you like to add:  ")
            animals , plants = day(many, animals, plants)
# =============================================================================
#     add_species(animals, "Human", Human, n)
#     add_species(animals, "Wolf", Wolf, 10)
#     add_species(animals, "Cow", Cow, 0)
#     
#     printout(animals)
#     
#     for i in range(7):
#         #print (plants)
#         plants += growth(animals, "age") # "age" passed to increase age
#         plants = eat(animals, plants) # eating grass add top plant material, hunting
#         plants += growth(animals) #checking if died from starvation
#         printout(animals)
# 
#     breeding(animals, "Wolf")
#     print("\n\n\n\END")    
#     printout(animals)
#     print(f'Current plant food: {plants}')
# =============================================================================


def print_subclasses():
    subclasses = Animal.__subclasses__()

    # Define column widths, ensuring there's enough space for each column
    class_width = max(len(subclass.__name__) for subclass in subclasses)
    lifespan_width = max(len(str(subclass(age=0, satiation=100, sex='m').lifespan)) for subclass in subclasses)
    habitat_width = max(len(subclass(age=0, satiation=100, sex='m').habitat) for subclass in subclasses) + 2
    weight_width = max(len(f"{subclass(age=0, satiation=100, sex='m').weight:.2f}") for subclass in subclasses)
    eating_width = max(len(subclass(age=0, satiation=100, sex='m').eating) for subclass in subclasses)

    # Print table header
    print(f"{'Class':<{class_width}} | "
          f"{'Lifespan':<{lifespan_width}} | "
          f"{'Habitat':<{habitat_width}} | "
          f"{'Weight':<{weight_width}} | "
          f"{'Eating':<{eating_width}}")

    # Print table separator
    print(f"{'-' * class_width} | "
          f"{'-' * lifespan_width * 4} | "
          f"{'-' * habitat_width} | "
          f"{'-' * weight_width} | "
          f"{'-' * eating_width}")

    # Print table rows
    for subclass in subclasses:
        obj = subclass(age=0, satiation=100, sex='m')
        print(f"{subclass.__name__:<{class_width}} | "
              f"{obj.lifespan:<{lifespan_width * 4}} | "
              f"{obj.habitat:<{habitat_width}} | "
              f"{obj.weight:>{weight_width}.2f} | "
              f"{obj.eating:<{eating_width}}")


def day(days, animals, plants):
    for i in range(days):
        plants += growth(animals, "age") # "age" passed to increase age
        plants = eat(animals, plants) # eating grass add top plant material, hunting
        plants += growth(animals) #checking if died from starvation
    print(f'\033[92m---{days} day(s) had passed---\033[0m')
    print ("Current habitats:")
    printout(animals)
    print(f'\nCurrent number of plants is: {plants}')
    return animals, plants
    

def eat(animals, plant):
    lprey = []
    for species in animals: #herbivoars eat first
        for obj in animals[species]:
            if obj.eating == "plants":
                lprey.append(obj)
                if plant == 0:
                    obj.satiation -= 9
                else:
                    obj.satiation += 26
                    plant -= 1
    
    for species in animals:
        deads = []
        for obj in animals[species]:
            if obj.eating == "meat":
                if lprey != []:
                    if np.random.randint(2) == 1:
                        prey = random.choice(lprey)
                        deads.append(prey)
                        obj.satiation += 53
                        print(f'\n{prey} was killed.')
                        del lprey[lprey.index(prey)]
                    else:
                        obj.satiation -= 16
                else:
                    obj.satiation -= 9
        
        for hunted in deads:
            for each in animals:
                if hunted in animals[each]:  # checking if dead-ones are in list
                    animals[each].remove(hunted)
    
    return plant
    
    


def add_species(animals, species_name, cls, count, sat = 100):
    species_list = []
    for i in range(count):
        species_list.append(cls(age= 0, satiation = sat, sex = random.choice(POL)))
    if species_name in animals:
        animals[species_name].extend(species_list)
    else:
        animals[species_name] = species_list


def printout(animals):
    empty = 1
    for species in animals:
        if len(animals[species]) > 0:
            num = 1
            print(f"\nSpecies: {species}\n")
            empty = 0
        for individual in animals[species]:
            print(f'#{num} {individual}')
            num += 1
    if empty:
        print("None")
        
def breeding(animals, species_name):
    
    male = False
    female = False
    breed = 0
    newbsat = 0
    if len(animals[species_name]) < 2:
        print(f'\033[91m#Error# Breeding failure.\nYou need more {species_name} to breed.\033[0m')
    else:
        
        for obj in animals[species_name]:
           
            # conditions for water
            if obj.habitat == "water" and obj.satiation > 50:
                breed = 10
                newbsat = 23
                #diff sex check
                if obj.sex == "f":
                    female = True
                elif obj.sex == "m":
                    male = True
            # condition for air
            if obj.habitat == "air" and obj.satiation > 42 and obj.age > 3:
                breed = 4
                newbsat = 64
                #diff sex check
                if obj.sex == "f":
                    female = True
                elif obj.sex == "m":
                    male = True
            # condition for land 
            if obj.habitat == "land" and obj.satiation > 20 and obj.age > 5:
                breed = 2
                newbsat = 73
                #diff sex check
                if obj.sex == "f":
                    female = True
                elif obj.sex == "m":
                    male = True
                
        if male and female and breed != 0:
            print("\033[92m\n---Breeding was successful---\n\033[0m")
            add_species(animals, species_name, type(animals[species_name][0]), breed, newbsat) #type for passing Class without calling a map
        elif male and female:
            print("\033[91m#ERROR# Breeding failure.\nAll the {species_name} are of the same sex.\033[0m")


def growth(animals, age = 0):
    newplant = 0
    for species in animals:
        deads = []
        
        for obj in animals[species]:
            if age == "age":    
                setattr(obj, age, getattr(obj, age) + 1)
            mass = obj.death()
            if mass > 0:
                newplant += mass
                deads.append(obj)
                    
        for obj in deads:
            animals[species].remove(obj)
                    
    if newplant != 0:
        return newplant
    else:
        return 0           
                
def incheck(text):

    while True:
        num = input(text)
        if num.isdigit():
            if int(num) != 0:
                return int(num)
            else:
                print("\033[91m#ERROR# Zeros don't do anything, try something else\033[0m")
        else:
            print("\033[91m#ERROR# Your input doesn't fit...\033[0m")


def class_from_name(name): #map for getting class from name
    clss = {
        "Human": Human,
        "Wolf": Wolf,
        "Cow": Cow,
        "Sheep": Sheep,
        "Alligator": Alligator,
        "Salmon": Salmon,
        "Piranha": Piranha,
        "Trout": Trout,
        "Eagle": Eagle,
        "Pigeon": Pigeon,
        "Sparrow": Sparrow,
        "Hummingbird": Hummingbird
    }
    return clss.get(name)

    
    
    
class Animal:
    
    MAX_SATIATION = 100
    
    def __init__(self, age, lifespan, habitat, satiation, sex, weight, eating):
        self.age = age
        self.lifespan = lifespan
        self.habitat = habitat
        self._satiation = satiation  # Use a private attribute
        self.sex = sex
        self.weight = weight
        self.eating = eating
    
    @property
    def satiation(self):
        return self._satiation
    
    @satiation.setter #setter
    def satiation(self, value):
        self._satiation = min(value, self.MAX_SATIATION)
         
         
    def __str__(self):  
        return "AGE: " + str(self.age) + " | SATIATION: " + str(self.satiation) + "% | SEX: " + self.sex + " "
    
    def death(self):
        
        if self.age == self.lifespan or self.satiation < 10:
            weight = self.weight
            return weight
            
        else:
            return 0

class Human(Animal):
    def __init__(self, age, satiation, sex):
        super().__init__(
            age = age,
            lifespan = 70,
            habitat = "land",
            satiation = satiation,
            sex = sex,
            weight = 65,
            eating = "meat"
        )

class Wolf(Animal):
    def __init__(self, age, satiation, sex):
        super().__init__(
            age = age,
            lifespan = 16,
            habitat = "land",
            satiation = satiation,
            sex = sex,
            weight = 40,
            eating = "meat"
        )

class Cow(Animal):
    def __init__(self, age, satiation, sex):
        super().__init__(
            age = age,
            lifespan = 20,
            habitat = "land",
            satiation = satiation,
            sex = sex,
            weight = 750,
            eating = "plants"
        )

class Sheep(Animal):
    def __init__(self, age, satiation, sex):
        super().__init__(
            age = age,
            lifespan = 12,
            habitat = "land",
            satiation = satiation,
            sex = sex,
            weight = 70,
            eating = "plants"
        )

class Alligator(Animal):
    def __init__(self, age, satiation, sex):
        super().__init__(
            age = age,
            lifespan = 50,
            habitat = "water",
            satiation = satiation,
            sex = sex,
            weight = 230,
            eating = "meat"
        )

class Salmon(Animal):
    def __init__(self, age, satiation, sex):
        super().__init__(
            age = age,
            lifespan = 4,
            habitat = "water",
            satiation = satiation,
            sex = sex,
            weight = 14,
            eating = "plants"
        )

class Piranha(Animal):
    def __init__(self, age, satiation, sex):
        super().__init__(
            age = age,
            lifespan = 10,
            habitat = "water",
            satiation = satiation,
            sex = sex,
            weight = 1.5,
            eating = "meat"
        )

class Trout(Animal):
    def __init__(self, age, satiation, sex):
        super().__init__(
            age = age,
            lifespan = 11,
            habitat = "water",
            satiation = satiation,
            sex = sex,
            weight = 2,
            eating = "plants"
        )

class Eagle(Animal):
    def __init__(self, age, satiation, sex):
        super().__init__(
            age = age,
            lifespan = 20,
            habitat = "air",
            satiation = satiation,
            sex = sex,
            weight = 6.5,
            eating = "meat"
        )

class Pigeon(Animal):
    def __init__(self, age, satiation, sex):
        super().__init__(
            age = age,
            lifespan = 6,
            habitat = "air",
            satiation = satiation,
            sex = sex,
            weight = 0.35,
            eating = "plants"
        )

class Sparrow(Animal):
    def __init__(self, age, satiation, sex):
        super().__init__(
            age = age,
            lifespan = 3,
            habitat = "air",
            satiation = satiation,
            sex = sex,
            weight = 0.03,
            eating = "plants"
        )

class Hummingbird(Animal):
    def __init__(self, age, satiation, sex):
        super().__init__(
            age = age,
            lifespan = 5,
            habitat = "air",
            satiation = satiation,
            sex = sex,
            weight = 0.004,
            eating = "plants"
        )

if __name__ == "__main__":
    main()
    