# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:08:16 2022
Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns
needed for a cookout, with the minimum amount of leftovers.

The program should ask the user for the number of people attending the cookout and the number of hot dogs
 each person will be given.

Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8.

The program should display the following details:

• The minimum number of packages of hot dogs required
• The minimum number of packages of hot dog buns required
• The number of hot dogs that will be left over
• The number of hot dog buns that will be left over

@author: argue
"""

hot_dogs_in_pack =10
buns_in_pack = 8

num_people_attending = int(input('Number of people attending the cookout: '))
num_hot_dogs_per_person = int(input('How many hot dogs will each person be given: '))


import math

num_hot_dogs = int(num_people_attending * num_hot_dogs_per_person) 
packs_hot_dogs = int(num_hot_dogs/hot_dogs_in_pack)
whole_packs_hot_dogs = int(math.ceil(packs_hot_dogs + (num_hot_dogs % hot_dogs_in_pack > 0)))
print(f'\nThe minimum number of packages of hot dogs required is: {whole_packs_hot_dogs}.')

num_buns = int(num_hot_dogs)
packs_buns = int(num_buns/buns_in_pack)
whole_packs_buns= int(math.ceil(packs_buns + (num_buns % buns_in_pack> 0)))
print(f'The minimum number of packages of hot dog buns required is: {whole_packs_buns}.')

leftover_hotdogs =  num_hot_dogs % hot_dogs_in_pack
if leftover_hotdogs != 0:
    print(f'The number of hot dogs that will be leftover is: {leftover_hotdogs}.')
else:
    print('There are 0 leftover hot dogs!')

leftover_buns = num_buns % buns_in_pack
if leftover_buns != 0:
    print(f'The number of hot dog buns that will be leftover is: {leftover_buns}.')
else:
    print('There are 0 leftover hot dog buns!')