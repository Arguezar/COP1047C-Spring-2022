# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:36:54 2022

@author: Arguez, Arlene
"""
#All taxpayers are charged a 
#All taxpayers are allowed a $10,000 standard deduction
#For each dependent, a taxpayer is allowed an additional $3,000 deduction
#Gross income must be entered to the nearest penny
#The income tax is expressed as a decimal number

gross_income = float(input('Enter the gross income: '))
dependents = int(input('Enter the number of dependents: '))
flat_tax_rate = float(.20)
standard_deduction = (10000)
dependent_deduction = dependents*3000
base_tax = (gross_income-standard_deduction)

if dependents > 0:
    income_tax = ((base_tax - dependent_deduction)*flat_tax_rate)
else:
    income_tax = base_tax*flat_tax_rate

print (f'The income tax is ${income_tax:.1f}')