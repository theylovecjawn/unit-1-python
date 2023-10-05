"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
my_string = "Caleb" #Creation of my string with random items inside

for i in my_string: #for loop using i as the characters in the list
    print(i) #prints the items in the list

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
num_list = [1,2,3,4,5] # Making the list of numbers to add
sum = 0 # setting the original sum to 0
for x in num_list: #for all  the items in numbered list this runs
    sum += x #adds all the items in num_list 
print(sum) #prints the total

"""
Exercise 3:
Write a program to find and print the length of each word in a sentence using a for loop and a list.
"""
sentence = 'The quick brown fox jumped over the lazy dog' #creation of the sentence 
words = sentence.split( )

for p in words: #Creating the for loop using p as the items in the sentence
    print("The length of", p, "is: ", len(p)) #Prints the length of the words

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
fruits = {
    'apples': 6,
    'mangos': 2,
    'oranges': 9,
    'plumbs': 7,
    'grapes': 3
} # Fruits dictionary creation
for item in fruits:
    print(item)

    # The output is the keys being printed on differnt lines. This is exactly what I thought would happen because we never did specify what exactly we wanted to print, we just said to print the items within the dictionary.