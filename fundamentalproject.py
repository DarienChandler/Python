#!/bin/python3
"""
Created on Thu Sep  2 13:32:54 2021

@author: Darien
"""
"""
Python Fundamentals 

Goal: be able to demonstrate use of python basic and functions 

PseudoCode 

-Display a welcome
-display a list task to perform   
* Make function for each task

-Prompt Choice of task
-Perform task 

 
"""
"""
- Useful Links - 
1.https://www.w3schools.com/python/

"""
# Modules 


# Functions
def menu():
    print("[1] Option 1: Addition")
    print("[2] Option 2: Subtract")
    print("[3] Option 3: Multiply")
    print("[4] Option 4: Divide")
    print("[5] Option 5: Break Function Exit")
    print("[6] Option 6: Files")
    print("[7] Option 7: ")
    print("[8] Option 8: Strings")
    print("[0] Exit the program")

def option1():
    print("You have choosen addition ")
    x, y = input("Enter two values to add : ").split()
    x = int (x)
    y = int (y)
    z = x + y
    print("The value of the two numbers added equals", z)
    print()
       
       

def option2():
    print("You have choosen subtraction ")
    x, y = input("Enter two values to subtract : ").split()
    x = int (x)
    y = int (y)
    z = x - y
    print("The value of the two numbers sub equals", z)
    print()
       
    
def option3():
    print("You have choosen multiplication")
    x, y = input("Enter two values to multiply : ").split()
    x = int (x)
    y = int (y)
    z = x * y
    print("The value of the two numbers multiplied equals", z)
    print()
       
    
def option4():
    print("You have chosen division") 
    x, y = input("Enter two values to divide : ").split()
    x = int (x)
    y = int (y)
    z = x / y
    print("The value of the two numbers divided it", z)
    print()

def option6():
    print("You have need to access files ") 
    x = input("Enter 1, if you would like to write to an existing file. Enter 2, if you would like to make a new file: ")
    x = int (x)
    # y = int (y)
  
    if x == 1:
        print("\n")
        print("You made the decision to write into an existing file")
        file = input("Enter the name of file: ")
        with open (file,"a") as f:
            y = input("What would you like to add to: " + str(f) + "?: ")
            f.writelines(y)
            f.write("\n")
            print("You have successfully written on" + str(f) + "!")
            
    elif x == 2:
        print("\n")
        print("Decision to make a new file ")
        print("\n")
        y = input(" What would you like to name this file:  ")
        f = open (y,"x")
        print("You have successfully created file: " + str(y) + "!")
    else:
        print("Invalid option")
        


    
   
# Start of function  
menu()
option = int(input("Enter your option:  "))
print("\n")

while option != 0:
    if option == 1:
        #do option 1 stuff
        option1()
    
    elif option == 2:
        #do option 2 stuff
        option2()
    
        
             
    elif option == 3:
        #do option 3 stuff
        option3()
         
    elif option == 4:
        #do option 4 stuff
        option4()

    elif option == 5:
        #do option 5 stuff
        print(" I currently do not have a function made")
        print(" I break out of loop using break function")
        break 

    elif option == 6:
        #do option 4 stuff
        option6()

    elif option == 7:
        #do option 4 stuff
        option7()

    else: 
        print("Invalid option ")
    
    print()    
    menu()
    option = int(input("Enter your option:  "))        

print("Thanks for using this program.  Goodbye. ")
# End of code 
