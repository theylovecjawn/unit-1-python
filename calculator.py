import math #importing math!

def calculation(): #function for calculations
    if userinp == "add": #adds the two numbers
        print(num1 + num2)
    elif userinp == 'sub':#subtracts the two numbers
        print(num1 - num2)
    elif userinp == 'mult':#multiplies the two numbers
        print(num1 * num2)
    elif userinp == 'div':#divides the two numbers
        if num2 == 0:
            print("This can't be done:")
        else:
            print(num1 / num2)
    elif userinp == 'flrdiv':#Floor Divides the two numbers
        if num2 == 0:
            print("This can't be done:")
        else:
            print(num1 // num2)
    elif userinp == 'expo':#Does the exponents of the two numbers
        print(num1 ** num2)
    elif userinp == 'remain': #gets the remainder of the two numbers
        print(num1 % num2)
          

print("Welcome to the Calculatinator-inator 9000 V1!") #Welcome message


num1 = float(input("Enter the first number: ")) #asking for the integer value for the first number
num2 = float(input("Enter the second number: ")) #asking for the integer value for the second number



print('''
Index: 

add = Addition
sub = Subtraction
mult = Multiplication
div = Division
flrdiv = Floor Division
expo = Expontents
remain = Remainder
''') # creating the key for user inrterface

print("Please select an opperation (case sensitive):") # Telling them to choose

userinp = input('Pick: ')#asks user for the opperation they want to pick

calculation() # running function defined earlier

