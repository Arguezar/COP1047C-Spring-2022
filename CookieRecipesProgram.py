# Uses Python library, Pandas, that contains a set of functions and specialised data structures
import pandas as pd
# Uses an excel spreadsheet were Cookies recipes (data) is stored
df = pd.read_excel (r'CookieRecipes.xlsx') 
# Function displays cookies list, values from spreadsheet rows/columns by integer position, option to exit program
def print_cookies():
    print("\n\t[1]", df.iat[1,0], "\n\t[2]", df.iat[2,0],"\n\t[3]", df.iat[3,0],
      "\n\t[4]", df.iat[4,0],"\n\t[5]", df.iat[5,0], "\n\t[6]", df.iat[6,0])
    print("\n\t[0] EXITs the program.")
# Welcome statement with instruction for selection, requires user input
print("\nWelcome to Group 3's Cookie Recipes Program!")
print ("\nThis program has yummy cookie recipes for you to choose from:")
print_cookies()
# Request for cookie recipe selection, requires User input 
#Ask for specific input as number 1-6, any other character generates value error statement
while True:
  try:
      option = int(input("Enter your choice (1-6 or 0 to exit): ")) 
      break
  except ValueError:
     print("\nOops...That's not a number!")
# If user enters 0 to exit, prints Exit statement, ends program
while option == 0:            
    if option == 0 :
        del df
        print("\nGoodbye! Come back when you get a craving for cookies!")
        break
# If user enters number not in list, prints comment to enter number in list.
while  option < 0 or option > 6:
        print("\nThe number",option,"is not an option, please choose a number in the list.")
        option = int(input("Enter your choice (1-6 or 0 to exit): "))
# If user enters a valid number from list, shows Cookie name, Prep Time, Cook Time and Yield amount 
else:
    print("\n\n"'{:*^150}'.format("*"))
    print("\n\n", df.iat[option,0])
    print("\n\tPrep Time:",int(df.iat[(option),16]),"mins","\tCook Time (per sheet):",int(df.iat[(option),17]),
           "mins","\tYields:",int(df.iat[(option),18]),"cookies","\n\nIngredients needed for one batch:\n")
from fractions import Fraction
# Checks that each ingredient amount not equal to zero, converts and splits float to fraction and determines statement dependent on amount
if (df.iat[(option),1] != 0):
    if (df.iat[(option),1] < 1):
        print("\t",Fraction(df.iat[(option),1]% 1),'\t{:<45}'.format("cup of All-Purpose Flour"))         
    else:
        i, d = divmod(df.iat[(option),1], 1)
        if (d != 0):
                print("\t",int(i),Fraction(d),'\t{:<45}'.format("cup(s) of All-Purpose Flour"))
        else: 
                print("\t",int(i),'{:<45}'.format("cup(s) of All-Purpose Flour"))
if (df.iat[(option),2] != 0):
    if (df.iat[(option),2] < 1):
        print("\t",Fraction(df.iat[(option),2]% 1),'{:<45}'.format("tsp of Baking Powder"))
    else:
        i, d = divmod(df.iat[(option),2], 1)
        if (d != 0):
                print("\t",int(i),Fraction(d),'{:<45}'.format("tsp(s) of Baking Powder"))  
        else: 
                print("\t",int(i),'{:<45}'.format("tsp(s) of Baking Powder"))
if (df.iat[(option),3] != 0):
    if (df.iat[(option),3] < 1):
        print("\t",Fraction(df.iat[(option),3]% 1),'{:<45}'.format("cup of Baking Soda"))
    else:
        i, d = divmod(df.iat[(option),3], 1)
        if (d != 0):
                print("\t",int(i),Fraction(d),'{:<45}'.format("tcup(s) of Baking Soda"))
        else: 
                print("\t",int(i),'{:<45}'.format("cup(s) of Baking Soda"))
if (df.iat[(option),4] != 0):
    if (df.iat[(option),4] < 1):
        print("\t",Fraction(df.iat[(option),4]% 1),'{:<40}'.format("cup of Brown Sugar (packed)"))         
    else:
        i, d = divmod(df.iat[(option),4], 1)
        if (d != 0):
                print("\t",int(i),Fraction(d),'{:<40}'.format("cup(s) of Brown Sugar (packed)")) 
        else: 
                print("\t",int(i),'{:<40}'.format("cup(s) of Brown Sugar (packed)"))
if (df.iat[(option),5] != 0):
    if (df.iat[(option),5] < 1):
        print("\t",Fraction(df.iat[(option),5]% 1),'{:<45}'.format("cup of Butter"))
    else:
        i, d = divmod(df.iat[(option),5], 1)
        if (d != 0):
                print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of Butter"))
        else: 
                print("\t",int(i),'{:<45}'.format("cup(s) of Butter"))
if (df.iat[(option),6] != 0):
    if (df.iat[(option),6] < 1):
        print("\t",Fraction(df.iat[(option),6]% 1),'{:<45}'.format("cup of Chocolate Chips"))          
    else:
        i, d = divmod(df.iat[(option),6], 1)
        if (d != 0):
                print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of Chocolate Chips"))  
        else: 
                print("\t",int(i),'{:<45}'.format("cup(s) of Chocolate Chips"))
if (df.iat[(option),7] != 0):
    if (df.iat[(option),7] < 1):
        print("\t",Fraction(df.iat[(option),7]% 1),'{:<45}'.format("cup of Chopped Pecans"))          
    else:
        i, d = divmod(df.iat[(option),7], 1)
        if (d != 0):
                print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of Chopped Pecans")) 
        else: 
                print("\t",int(i),'{:<45}'.format("cup(s) of Chopped Pecans"))
if (df.iat[(option),8] != 0):
    if (df.iat[(option),8] < 1):
        print("\t",Fraction(df.iat[(option),8]% 1),'{:<45}'.format("of an Egg White"))
    else:
        i, d = divmod(df.iat[(option),8], 1)
        if (d != 0):
                print("\t",int(i),Fraction(d),'{:<45}'.format("of Egg White(s)"))
        else: 
                print("\t",int(i),'{:<45}'.format("Egg White(s)"))
if (df.iat[(option),9] != 0):
    if (df.iat[(option),9] < 1):
        print("\t",Fraction(df.iat[(option),9]% 1),'{:<45}'.format("of an Egg"))
    else:
        i, d = divmod(df.iat[(option),9], 1)
        if (d != 0):
                print("\t",int(i),Fraction(d),'{:<45}'.format("\tEgg(s)"))  
        else: 
                print("\t",int(i),'{:<45}'.format("\tEgg(s)"))
if (df.iat[(option),10] != 0):
    if (df.iat[(option),10] < 1):
        print("\t",Fraction(df.iat[(option),10]% 1),'{:<45}'.format("cup of Oatmeal"))
    else:
        i, d = divmod(df.iat[(option),10], 1)
        if (d != 0):
                print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of Oatmeal"))
        else: 
                print("\t",int(i),'{:<45}'.format("cup(s) of Oatmeal"))
if (df.iat[(option),11] != 0):
    if (df.iat[(option),11] < 1):
        print("\t",Fraction(df.iat[(option),11]% 1),'{:<45}'.format("cup of Peanut Butter"))
    else:
        i, d = divmod(df.iat[(option),11], 1)
        if (d != 0):
                print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of Peanut Butter"))
        else: 
                print("\t",int(i),'{:<45}'.format("cup(s) of Peanut Butter"))
if (df.iat[(option),12] != 0):
    if (df.iat[(option),12] < 1):
        print("\t",Fraction(df.iat[(option),12]% 1),'{:<45}'.format("tsp of Salt"))
    else:
        i, d = divmod(df.iat[(option),12], 1)
        if (d != 0):
                print("\t",int(i),Fraction(d),'{:<45}'.format("tsp(s) of Salt"))
        else: 
                print("\t",int(i),'{:<45}'.format("tsp(s) of Salt"))
if (df.iat[(option),13] != 0):
    if (df.iat[(option),13] < 1):
        print("\t",Fraction(df.iat[(option),13]% 1),'{:<45}'.format("tsp of Vanilla Extract"))
    else:
        i, d = divmod(df.iat[(option),13], 1)
        if (d != 0):
                print("\t",int(i),Fraction(d),'{:<45}'.format("tsp(s) of Vanilla Extract"))
        else: 
                print("\t",int(i),'{:<45}'.format("tsp(s) of Vanilla Extract"))
if (df.iat[(option),14] != 0):
    if (df.iat[(option),14] < 1):
        print("\t",Fraction(df.iat[(option),14]% 1),'{:<45}'.format("cup of Sugar"))
    else:
        i, d = divmod(df.iat[(option),14], 1)
        if (d != 0):
                print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of Sugar"))
        else: 
                print("\t",int(i),'{:<45}'.format("cup(s) of Sugar"))
# Request for batch quantity, requires User input as number, any other character generates value error statement
while True:
  try:
      batchQty = float(input("\nHow many batches would you like to make? (minimum 1 batch, 2 for double, etc. or 0 to exit):" ))
      break
  except ValueError:
     print("\033[3m\nOops...That's not a number!\x1B[0m")
# if batch quantity is less than zero, prints statement and batch quantity is requested from user again
while batchQty == 0:            
    if batchQty == 0 :
        del df
        print("\nGoodbye! Come back when you get a craving for cookies!")
        break
while  batchQty < 0 or batchQty < 1:
            print("\033[3m\nDon\'t be Silly! It is not possible to make",batchQty,"\033[3mbatches of Cookies.\x1B[0m")
            batchQty = float(input("\nHow many batches would you like to make? (minimum 1 batch, 2 for double, etc. or 0 to exit):" ))
    # If batch quantity is equal to or higher than one, prints statement showing Cookie selected, batch quantity entered and updated: Prep Time, Yield amount
else:
    print("\n\n"'{:*^150}'.format("*"))
    print("\nTo make", batchQty, "batches of",df.iat[(option),0],"you will need:")
    print("\n\tPrep Time:",int(df.iat[(option),16]*batchQty),"mins","\tCook Time (per sheet):",int(df.iat[(option),17]),
        "mins","\tYields:",int(df.iat[(option),18]*batchQty),"cookies","\n\nIngredients needed for",batchQty,"batches:\n")
# Prints updated ingredient amounts by multiplying original amounts by batch quantity inputted by User
# Checks that each ingredient amount not equal to zero is converted and splits float to fraction and determines statement dependent on amount
if (df.iat[(option),1]*batchQty != 0):
    if (df.iat[(option),1]*batchQty < 1):   
        print("\t",Fraction(df.iat[(option),1]% 1)*batchQty,'{:<45}'.format("cup of All-Purpose Flour"))
    else:
        i, d = divmod(df.iat[(option),1]*batchQty, 1)
        if (d != 0):
            print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of All-Purpose Flour"))
        else: 
            print("\t",int(i),'{:<45}'.format("cup(s) of All-Purpose Flour"))
if (df.iat[(option),2]*batchQty  != 0):
    if (df.iat[(option),2]*batchQty  < 1):
            print("\t",Fraction(df.iat[(option),2]% 1)*batchQty ,'{:<45}'.format("tsp of baking powder"))
    else:
          i, d = divmod(df.iat[(option),2]*batchQty , 1)
          if (d != 0):
              print("\t",int(i),Fraction(d),'{:<45}'.format("tsp(s) of baking powder"))
          else: 
              print("\t",int(i),'{:<45}'.format("tsp(s) of baking powder"))
if (df.iat[(option),3] != 0):
    if (df.iat[(option),3]*batchQty  < 1):
        print("\t",Fraction(df.iat[(option),3]% 1)*batchQty ,'{:<45}'.format("cup of Baking Soda"))
    else:
          i, d = divmod(df.iat[(option),3]*batchQty , 1)
    if (d != 0):
        print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of Baking Soda"))
    else: 
        print("\t",int(i),'{:<45}'.format("cup(s) of Baking Soda"))
if (df.iat[(option),4]*batchQty  != 0):
    if (df.iat[(option),4]*batchQty  < 1):
        print("\t",Fraction(df.iat[(option),4]% 1)*batchQty ,'{:<45}'.format("cup of Brown Sugar (packed)"))
    else:
            i, d = divmod(df.iat[(option),4]*batchQty , 1)
            if (d != 0):
                    print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of Brown Sugar (packed)"))
            else: 
                    print("\t",int(i),'{:<45}'.format("cup(s) of Brown Sugar (packed)"))
if (df.iat[(option),5]*batchQty != 0):
        if (df.iat[(option),5]*batchQty  < 1):
            print("\t",Fraction(df.iat[(option),5]% 1*batchQty ),'{:<45}'.format("cup of Butter"))
        else:
            i, d = divmod(df.iat[(option),5]*batchQty , 1)
            if (d != 0):
                    print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of Butter"))
            else: 
                    print("\t",int(i),'{:<45}'.format("cup(s) of Butter"))
if (df.iat[(option),6]*batchQty  != 0):
        if (df.iat[(option),6]*batchQty  < 1):
            print("\t",Fraction(df.iat[(option),6]*batchQty % 1),'{:<45}'.format("cup of Chocolate Chips"))        
        else:
            i, d = divmod(df.iat[(option),6]*batchQty , 1)
            if (d != 0):
                    print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of Chocolate Chips"))
            else: 
                    print("\t",int(i),'{:<45}'.format("cup(s) of Chocolate Chips"))
if (df.iat[(option),7]*batchQty  != 0):
        if (df.iat[(option),7]*batchQty  < 1):
            print("\t",Fraction(df.iat[(option),7]*batchQty % 1),'{:<45}'.format("cup of chopped Pecans"))     
        else:
            i, d = divmod(df.iat[(option),7]*batchQty , 1)
            if (d != 0):
                    print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of chopped Pecans"))
            else: 
                    print("\t",int(i),'{:<45}'.format("cup(s) of chopped Pecans"))
if (df.iat[(option),8]*batchQty  != 0):
        if (df.iat[(option),8]*batchQty  < 1):
            print("\t",Fraction(df.iat[(option),8]*batchQty % 1),'{:<45}'.format("of an Egg White"))
        else:
            i, d = divmod(df.iat[(option),8]*batchQty , 1)
            if (d != 0):
                    print("\t",int(i),Fraction(d),'{:<45}'.format("of Egg White(s)"))
            else: 
                    print("\t",int(i),'{:<45}'.format("Egg White(s)"))
if (df.iat[(option),9]*batchQty  != 0):
        if (df.iat[(option),9]*batchQty  < 1):
            print("\t",Fraction(df.iat[(option),9]*batchQty % 1),'{:<45}'.format("of an Egg"))
        else:
            i, d = divmod(df.iat[(option),9]*batchQty , 1)
            if (d != 0):
                    print("\t",int(i),Fraction(d),'{:<45}'.format("\tEgg(s)"))
            else: 
                    print("\t",int(i),'{:<45}'.format("\tEgg(s)"))
if (df.iat[(option),10]*batchQty  != 0):
        if (df.iat[(option),10]*batchQty  < 1):
            print("\t",Fraction(df.iat[(option),10]*batchQty % 1),'{:<45}'.format("cup of Oatmeal"))
        else:
            i, d = divmod(df.iat[(option),10]*batchQty , 1)
            if (d != 0):
                    print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of Oatmeal"))
            else: 
                    print("\t",int(i),'{:<45}'.format("cup(s) of Oatmeal"))
if (df.iat[(option),11]*batchQty  != 0):
        if (df.iat[(option),11]*batchQty  < 1):
            print("\t",Fraction(df.iat[(option),11]*batchQty % 1),'{:<45}'.format("cup of Peanut Butter"))
        else:
            i, d = divmod(df.iat[(option),11]*batchQty , 1)
            if (d != 0):
                    print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of Peanut Butter"))
            else: 
                    print("\t",int(i),'{:<45}'.format("cup(s) of Peanut Butter"))
if (df.iat[(option),12]*batchQty  != 0):
        if (df.iat[(option),12]*batchQty  < 1):
            print("\t",Fraction(df.iat[(option),12]*batchQty % 1),'{:<45}'.format("tsp of Salt"))
            i, d = divmod(df.iat[(option),12]*batchQty , 1)
            if (d != 0):
                    print("\t",int(i),Fraction(d),'{:<45}'.format("tsp(s) of Salt"))
            else: 
                    print("\t",int(i),'{:<45}'.format("tsp(s) of Salt"))
if (df.iat[(option),13]*batchQty  != 0):
        if (df.iat[(option),13]*batchQty  < 1):
            print("\t",Fraction(df.iat[(option),13]*batchQty % 1),'{:<45}'.format("tsp of Vanilla Extract"))
        else:
            i, d = divmod(df.iat[(option),13]*batchQty , 1)
            if (d != 0):
                    print("\t",int(i),Fraction(d),'{:<45}'.format("tsp(s) of Vanilla Extract"))
            else: 
                    print("\t",int(i),'{:<45}'.format("tsp(s) of Vanilla Extract"))
if (df.iat[(option),14]*batchQty  != 0):
        if (df.iat[(option),14]*batchQty  < 1):
            print("\t",Fraction(df.iat[(option),14]*batchQty % 1),'{:<45}'.format("cup of Sugar"))
        else:
            i, d = divmod(df.iat[(option),14]*batchQty , 1)
            if (d != 0):
                    print("\t",int(i),Fraction(d),'{:<45}'.format("cup(s) of Sugar"))
            else: 
                    print("\t",int(i),'{:<45}'.format("cup(s) of Sugar"))
# Prints Directions for making the Cookie Recipe selected by User, adds one of two closing statements
print()
print("Here are the directions:\n\n\t",df.iat[(option),20])
print("\n\n"'{:*^150}'.format("*"))
if batchQty >= 4:
    print("\n\nEnjoy your",int(df.iat[(option),18]*batchQty),(df.iat[option,0]).rstrip(),(", please share!!!!").lstrip(' '))
#Prints exit statement
else:
        print("\n",(df.iat[(option),0]).rstrip(" "),("are Yummy, Enjoy!!").lstrip(' '))
#Prints exit statement        
print("\n"'{:^150}'.format("Goodbye! Come back when you get another craving for cookies!"))
print()