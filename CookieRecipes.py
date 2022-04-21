# Uses Python library, Pandas, that contains a set of functions and specialised data structures
import pandas as pd

# Uses an excel spreadsheet were Cookies data is stored
df = pd.read_excel (r'C:\CookieRecipes.xlsx') 

# Function to print list of cookies and how to end the program
# Selects the values for rows/columns by integer position from excel spreadsheet
def print_cookies():
    print("\n\t[1]", df.iat[1,0], "\n\t[2]", df.iat[2,0],"\n\t[3]", df.iat[3,0],
      "\n\t[4]", df.iat[4,0],"\n\t[5]", df.iat[5,0], "\n\t[6]", df.iat[6,0])
    print("\t\t[0] Exits the program.")

# Welcome statement with instruction for selection, requires user input
print("\nWelcome to Group 3's Cookie Recipes Program!")
print ("\nThis program has yummy cookie recipes for you to choose from:")
print_cookies()
#Ask for specific input as number 1-6, any other character generates value error statement
while True:
  try:
      option = int(input("Enter your choice (1-6 or 0 to exit): ")) 
      break
  except ValueError:
     print("That's not a number!")
    
# If user enters 0 to exit, prints Exit statement, ends program
while option == 0:            
    if option == 0 :
        del df
        print("\nGoodbye! Come back when you get a craving for cookies!")
        break
# If user enters number not in list, prints comment to enter number in list.
while  option < 0 or option >6:
        print("\nThere is no number",option,"please choose a number in the list.")
        option = int(input("Enter your choice (1-6 or 0 to exit): "))
# If user enters a valid number from list, shows Cookie name, Prep Time, Cook Time and Yield amount 
else:
     print("\n\n", df.iat[option,0])
     print("\n\tPrep Time: ", int(df.iat[(option),16]),"mins","\tCook Time (per sheet): ", int(df.iat[(option),17]),
           "mins","\tYeilds: ", int(df.iat[(option),18])," cookies","\n\nIngredients needed for one batch:\n")
# Checks that each ingredient amount not equal to zero, prints amount if true
     if (df.iat[(option),1] != 0):
         print("\t",df.iat[(option),1]," \tcups of All-Purpose Flour")  
     if df.iat[(option),2] != 0:
             print("\t",df.iat[(option),2]," \ttsps of baking powder") 
     if df.iat[(option),2] != 0:
             print("\t",df.iat[(option),2]," \ttsps of baking powder")   
     if df.iat[(option),3] != 0:
             print("\t",df.iat[(option),3]," \ttsps of baking soda")     
     if  df.iat[(option),4] !=0:
             print("\t",df.iat[(option),4]," \tcups of brown sugar (packed)")            
     if  df.iat[(option),5] !=0:
             print("\t",df.iat[(option),5]," \tcups of butter")
     if  df.iat[(option),6] !=0:
              print("\t",df.iat[(option),6]," \tcups of chocolate chips")
     if  df.iat[(option),7] !=0:
               print("\t",df.iat[(option),7]," \tcups of chopped pecans")   
     if  df.iat[(option),8] !=0:
               print("\t",df.iat[(option),8]," \tegg whites")
     if  df.iat[(option),9] !=0:
               print("\t",df.iat[(option),9]," \tegg(s)")
     if  df.iat[(option),10] !=0:
               print("\t",df.iat[(option),10]," \tcups of oatmeal")      
     if  df.iat[(option),11] !=0:
                print("\t",df.iat[(option),11]," \tcups of Peanut Butter")
     if  df.iat[(option),12] !=0:
                print("\t",df.iat[(option),12]," \ttsps of salt")
     if  df.iat[(option),13] !=0:
                print("\t",df.iat[(option),13]," \ttsps of vanilla extract")       
     if  df.iat[(option),14] !=0:
                print("\t",df.iat[(option),14]," \tcups of white sugar") 
# Request for batch quantity, requires User input                
batchQty = float(input("\nHow many batches would you like to make? (minimum 1 batch, 2 for double, etc.):" ))
# if batch quantity is less than zero, prints statement and batch quantity is requested from user again
while batchQty < 1:
        print("\nDon\'t be Silly! It is not possible to make",batchQty,"batches of Cookies.")
        batchQty = float(input("\nHow many batches would you like to make? (minimum 1 batch, 2 for double, etc.):" ))
# If batch quantity is greater or equal to one, prints statement showing batchqty entered,updated: Prep Time, Yield amount
else:
    print("\n\nTo make", batchQty, "batches of",df.iat[(option),0],"you will need:")
    print("\n\tPrep Time: ",int(df.iat[(option),16]*batchQty),"mins","\tCook Time (per sheet): ",int(df.iat[(option),17]),
    "mins","\tYields:",int(df.iat[(option),18]*batchQty),"cookies","\n\nIngredients needed for",batchQty,"batches:\n")
# Prints updated ingredient amounts by multiplying original amounts by batchqty inputed by User   
    if df.iat[(option),1] != 0:
        print("\t",(df.iat[(option),1])*batchQty," \tcups of All-Purpose Flour")  
    if df.iat[(option),2] != 0:
        print("\t",(df.iat[(option),2])*batchQty," \ttsps of baking powder") 
    if df.iat[(option),2] != 0:
        print("\t",(df.iat[(option),2])*batchQty," \ttsps of baking powder")   
    if df.iat[(option),3] != 0:
        print("\t",(df.iat[(option),3])*batchQty," \ttsps of baking soda")     
    if  df.iat[(option),4] !=0:
        print("\t",(df.iat[(option),4])*batchQty," \tcups of brown sugar (packed)")            
    if  df.iat[(option),5] !=0:
        print("\t",(df.iat[(option),5])*batchQty," \tcups of butter")
    if  df.iat[(option),6] !=0:
         print("\t",(df.iat[(option),6])*batchQty," \tcups of chocolate chips")
    if  df.iat[(option),7] !=0:
          print("\t",(df.iat[(option),7])*batchQty," \tcups of chopped pecans")   
    if  df.iat[(option),8] !=0:
          print("\t",(df.iat[(option),8])*batchQty," \tegg whites")
    if  df.iat[(option),9] !=0:
          print("\t",(df.iat[(option),9])*batchQty," \tegg(s)")
    if  df.iat[(option),10] !=0:
          print("\t",(df.iat[(option),10])*batchQty," \tcups of oatmeal")      
    if  df.iat[(option),11] !=0:
           print("\t",(df.iat[(option),11])*batchQty," \tcups of Peanut Butter")
    if  df.iat[(option),12] !=0:
           print("\t",(df.iat[(option),12])*batchQty," \ttsps of salt")
    if  df.iat[(option),13] !=0:
           print("\t",(df.iat[(option),13])*batchQty," \ttsps of vanilla extract")       
    if  df.iat[(option),14] !=0:
           print("\t",(df.iat[(option),14])*batchQty," \tcups of white sugar")
# Prints Directions for making the Cookie Recipe selected by User
print()
print('Here are the directions:\n\n\t',df.iat[(option),20],'\n\nEnjoy your',int(df.iat[(option),18]*batchQty),df.iat[option,0],'!!!!')
print()
