"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
for x in range(1,11): # Starts at 1 and goes to 10 because 11 is inlusive
    print(x) #Prints

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
print()
for i in range(900,1010, 10): #Starts at 900 and goes to 1000 because 1010 is inlusive and it is going up by 10
    print(i)

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
print()
for q in range(1,101, 9): #Starts at 1 and goes to 100 because 101 is inlusive and it is going up by 9
    print(q)
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
print()
sum = 0 #Sets the sum to 0 

for o in range(1,11): #Gets all the numbers from 1 --> 10 because 11 is inclusive
    sum += o #Adds each number as it goes up to 10
print(sum) #Prints the total sum
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""
print()
rows = 5
 
for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()

"""
Output:
* 
* * 
* * * 
* * * * 
* * * * * 

The output of the code is 15 stars split up into 5 different rows going from least to greatest.

The iterative process that this code executes is because since the row is set to 5, it is 5 seperate rows of  the stars. the "end"
makes it so that it is seperated right next to each other. There is a nested for loop with the value 1 being added to the variable 
created in the main range() statement which makes the rows have one added star to it.


"""