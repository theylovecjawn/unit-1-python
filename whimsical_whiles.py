import math
"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
x = 1

while x <= 10: # continues until x is equal 10 
    print(x) #prints x
    x += 1 #adds 1 to x

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
y = 10
while y >= 1: # continues until y is equal 1
    print(y) #prints y
    y -= 1 #subtracts 1 from y
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
num = int(input("Please input a number: ")) #Asked for an in for the input
factorial = 1 #sets the variable to 1
if num < 0: #if the number is 0 then it prints that it cant be done
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0: #if the num they enter is = to 0 then the factorial is 1
   print("The factorial of 0 is 1")
else: #if none of this is correct then we add one and multiply by it
   for i in range(1,num + 1): 
       factorial = factorial*i
   print("The factorial of: ",num,"is",factorial) #prints
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""


password = ['himathy99'] #makes password
guesses = 0
while guesses < 5: #Gives the user 5 chances
    for i in password : #Makes foorloop to see if the guess if in password
        guess = input('Please attempt to guess the password: ') #Creates the guess input
    if guess in password:
        print(' Correct! ' + guess + ' is the password: ') #if correct then it will print
        break #Stops the code
    else:
        print('Wrong. ') # if its wrong this prints
    guesses += 1 #adds 1 to the guesses

if guess in password:
  print()
else:
  print("Sorry you have no more tries") #prints when the tries are done

    

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
def takeSum(n): #creation of the takeSum() function
    
    sum = 0 #sets sum to 0
    while (n != 0): #While n parametr doesnt equal 0 then the following runs
       
        sum = sum + (n % 10) #sets the sum = to the sum plus the parameter modulus 10
        n = n//10 #floor divides the parameter n by 10 to
       
    return sum #returns the sum when this function is called
   
num = int(input('Please input a whole number: ')) #asks user for an int input
print(takeSum(num), "is the sum of the digits within this number") #calls and prints the function with input of the uses

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

