"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""

fruits = ['apple', 'orange','plum', 'mango'] #List of fruits
print(fruits) # Prints the list

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

fruits.append('banana') # I added "banana" to the list
print(fruits) # Printing out the new list with the added fruit

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""

fruits.remove('plum') #Deletes plum from the list
print(fruits) #Prints the list


"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

fruits[1] = 'starburst' #changes the oranges to starburst 
print(fruits) #prints the new list

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""

fruits.append('fortnite') # adding fortnite to list
fruits.append('gta') # adding gta to list
fruits.append('cars') # cars
print(fruits) #prints the new list
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del fruits[-1] #deletes the last item on the list
print(fruits) #prints the new list


"""
Task 7: Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""

x = fruits[:2] # takes the first 2 items in the list and stores it in the variable x
print(x) #prints the new list

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
cars_a = ['mercedes', 'honda', 'mclaren'] # making of the first list
cars_b = ['toyota', 'subaru', 'SUV'] # making of the second list

cars = cars_a + cars_b #extending the lists by joining them
print(cars) #prints the new list