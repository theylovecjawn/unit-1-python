'''Task 1: Greeting Function
 Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".'''

def greeting(name): #creates the function with the argument name 
    print("Hello, " + name)# prints hello plus the paremeter

greeting("Caleb") #calls the function with the name Caleb
'''
 Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.
'''
def sum_numbers(a, b): #creates the function with two arguments.
    print(a + b) # prints the sum of the two parameters

sum_numbers(2, 3) #calls the function with the two numbers 2 and 3

''' Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.'''
def factorial(num): #creates the funtion with a parameter of n
    fact = 1 #sets the variable to 1
    if num < 0: #if the number is 0 then it prints that it cant be done
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0: #if the num they enter is = to 0 then the factorial is 1
        print("The factorial of 0 is 1")
    else: #if none of this is correct then we add one and multiply by it
        for i in range(1,num + 1): 
            fact = fact*i
    print("The factorial of: ",num,"is",fact) #prints

factorial(5)

'''Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.
'''
def is_even(num): #creation of the function is_even with the 
    if num % 2 == 0:
        print('This is a even number') # if the modulus is = 0 then it is a even number
    else:
        print('This is an odd number') #If the modulus is not 0 then it will be an odd number

is_even(5) #calls the function with parameter 5
is_even(4)#calls the function with parameter 4

'''Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.'''

def calculate_area(length, width): #creates the calculate_area function with 2 parameters
    print(width * length) #prints the value of the wdith and lenegth multiplied together

calculate_area(5, 3) #calls the function with the parameters 5, and 3
