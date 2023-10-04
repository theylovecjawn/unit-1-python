todos = [] #creating an empty list for the todos
def show_the_todos():
    if not todos:
        print('Sorry there is no Todos.') #prints if there are no todo's
    else:
        for i, todo in enumerate(todos, start = 1): #Makes the list print with numbers starting next to it starting at 1
            print(f'{i}. {todo}')


while True: #Runs once the code is ran
    show_the_todos() #prints the Todos
    user_input = input('Would you like to add (type: "add") or remove (type: "remove") a todo?: ') #Asks the user if they would like to add/ remove
    if user_input == "add": #If the user types in add this runs
        new_todo = input('What is your new todo?: ') #Asks the user to type in the Todo they want.
        todos.append(new_todo) #adds to the end of the list
    elif user_input == "remove":#If the user types in remove this runs
        if len(todos) == 0: #Makes sure that the list has no items in it already
            print('Sorry you have no todos already.') #prints if there is no previous items in the list and they try to remove one
        else:
            remove_input = int(input("What would you like to remove? (give number of todo): " )) #Asks the uder for a number input to use to remove
            if remove_input <= 0: #Makes sure that the number inputted is  greater than 0
                print("Sorry You must input a number on the list.") #prints if this isnt greater than 0
            else: #runs if the numbevr is greater than 0
                del todos[remove_input - 1] #deletes the number on the list the uder inputs
 

    
    





