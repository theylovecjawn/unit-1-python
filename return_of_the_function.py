"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def sqaure_num(x): #creation of the sqaure_num function  
    return x**2 #gives the value back as the number sqaured

print(sqaure_num(2)) #prints the square number of 2 calling the sqaure_num function

"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def area_rect(z, y): #creation of the area_rect function 
    return z * y # gives back z * y

print(area_rect(3, 6)) #prints the area calling the function


"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

def cel_converter(ded): #Creation of the cel_converter function
    g = ded * 1.8 #g variable which holds the ded variable given and 1.8 multiplied together
    h = g + 32 #adds 32 to the and sets the value to the h 
    return h #returns the h value 

print(cel_converter(24)) #prints the value from cel. to far. of the value 24
    


"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

def average(q): #Creation of average function
   total = sum(q) #total is equal to the sum of all the numbers in the given paramter
   return total / len(q) # gives back the mean (all the numbers added up then divided by the number of the rest)
q = [1,2,3,4,5] # sets q to the list 1,2,3,4,5
print((average(q))) #prints the average using the function and giving it the q
    