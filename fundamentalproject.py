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
    print("[1] Option 1: New Variables ")
    print("[2] Option 2: Output and Input ")
    print("[3] Option 3: Operations ")
    print("[4] Option 4: Branching ")
    print("[5] Option 5: Loops ")
    print("[6] Option 6: Functions ")
    print("[7] Option 7: Aggregate Data ")
    print("[8] Option 8: Debugging ")
    print("[0] Exit the program ")

def option1():
    print("You have choosen New Variables ")
    print('''
          
   [-- New Variables --]
           (Attributes)
          Name: name of variable 
          Type: type of data does it contain
          Initial Value: variable's initial value
              
              
          Python Syntax { name = initValue }
           
          
          ''')
         
def option2():
    print("You have choosen Output & Input ")
    print('''
          
   [ -- Output  --]
                     (Attributes)
          Message: text to write to user 

          Python Syntax { print("message") }

   [-- Input --]
                     (Attributes)
          Variable: where the answer will be stored 
          Message: question being asked of the user 
              
          Python Syntax { variable = input("message") }
           
          
          ''')
           
def option3():
   print("You have choosen Operations ")
   print('''
          
    [-- Operations --]
          Things you do to variables. 
 
                     (Attributes)
        Numeric: add subtract multiply etc
        Text: combine, split, search, split, iterate, transform
        Conversion: convert from one type to another
        
                Python Syntax {}
        
        numeric: ( + , - , * , / , % , ** )
        text: splicing [0:5], 
        conversion: int(x), str(x), float(x)
        
                    
          ''')
    
def option4():
   print("You have choosen  Branching  ")
   print('''
          
    [ -- Branching  --]
                  (Attributes)
            Based on true/false expressions, how computers make decision
            Operators ( >= , <= , == , != , > , < ) * single = is for assignment 
            
            [-- If, Else, Elif --] 
                               
                      
                        { Python Syntax }
            #1 - If 
                
                if ( 5 > 3 ): 
                print("hello") 
                
            #2 - If, Else 
                
                if ( 3 == 2):
                    print("hello")
                else: 
                    print("false statement")
                
            #3 - If, Else, Elif 
                
                age  = 16
                if (age < 13):
                    print("you are young")
                elif (age >= 13 and age < 18):
                    print("you are a teenager")
                else: 
                    print("you are a adult")


    [ -- Try and excepts -- ] 

                    { Python Syntax }
            try: 
                if name > 3:
                    print("Hello")     
            except: 
                print("there is something wrong in code")           
          
          ''')

def option5():
   print("You have choosen Loops")
   print('''
          

     [ --  While loops --]
           
                (Attributes)
            sentry: variable that will control the loop 
            initilization code : code that maintains the sentry 
            condition: loop repeats if condition is true 
            change code: code to change sentry so that conditon can be triggered 
    
                    c = 0
                    while c < 5:
                        print(c)
                        c = c + 1

     [-- For Loops --]
    
                 (Attributes)
                sentry:will control the loop
                start: beginning value of sentry
                final: ending value of the sentry 
                change:integer to add to the sentry at each pass
                
                list1 = ["apples", "bananas", "cherries"]
                tup1 = (13,12,15)
                for item in list1:
                    print(item) >> prints out all contents 
                    
                for item in tup1:
                    print(item) >> prints out all contents 
                
                for i in range(0,10):
                    print(i) >> prints out first 9 numbers 0-9
        

    [-- Break, Continue, Pass --]

            c = 0
            while c < 5:
                print(c)
                c = c + 1
                if c == 3:
                    break
            
            while c <5: 
                c = c + 1
                if c ==2: 
                    continue 
                print(c)
                
            while c < 5:
                c = c + 1
                if c == 4:
                    pass
                print(c)
           
          
          ''')          

def option6():
   print("You have choosen Functions ")
   print('''
          
       [-- Functions --]
                     (Attributes)

        # Example 1
            def functname(): #creating a function
                print("hello world")  
            functname() # calling the function 
            
        # Example 2
            def greeting(name):
                print("Hello " + name + " Welcome!")
            greeting("darien")
            
            #3
            def add(x,y):
                print(x + y)
            add(2,2)
            
            #4
            def returnadd(x,y):
                return (x + y)    #After return python stops and does not run code after seeing return 
            sum = returnadd(12, 4)
            print(sum)


 [ -- 6B Built- In Functions  -- ]
            
            abs(x)
            bool(x)
            eval(x)
            exec(x)
            dir(str or x)
            help(variable.function(ex: upper))
            type(x) - get data type
            len(x) - get length 
           
          
          ''')          

def option7():
   print("You have chose Aggregate Data ")
   print('''
         
                [-- Aggregate Data --]
                     (Attributes)
              
            - data combined into a single variable 
            - Arrays - List - Dictionaries - Classes - Tuples
            
    [ -- List  - Mutable(can be changed) --] 
            
            shoplist = [ "apples", "oranges", "lemon",]
            shoplist.append - add item to the end of list 
            shoplist[0] = "new variable"
            del shoplist[x] = delete list at index
            len(shoplist)
            max or min(shoplist)
            
            
    [ -- Dictionaries - Key and Value  --]
            
            price = {"apples":1, "oranges":2, "lemon":4,}
            price["apple"] >>> 1
            price["apple"] = 1.50
            del price["lemon"]
                        
   [ -- Tuples - (Immutable - contents inside cannot change) --]
    * but you can add tuples together 
            
            tup = ( 'oranges' , 'apples', 'aappe') 
            tup[1]
                        
    [-- Classes --]
                        
            class Person:
                
                def getName(self):
                    print("Darien")
                def getAge(self):
                    print("16")
            
            p = Person()
            p.getName()
            p.getAge()

          ''') 

def option8():
   print("You have choosen Debugging ")
   print('''
          
                        (Attributes)
              
          Python Syntax { variable = input("message") }
           
          
          ''') 


    
   
# Start of function  
menu()
option = int(input("Enter your option:  "))
print("\n")

if option == 0:
    print("Thanks for using this program.  Goodbye. ")

elif option == 1:
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
        option5()

elif option == 6:
        #do option 4 stuff
        option6()

elif option == 7:
        #do option 4 stuff
        option7()
        
elif option == 8:
        #do option 4 stuff
        option8()
    
else: 
    print("You have entered an invalid option. Please try again. ")
    
    print()    
    menu()
    option = int(input("Enter your option:  "))        


# End of code  
