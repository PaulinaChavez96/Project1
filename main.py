from functions import get_todos, write_todos #this syntax can be used
# only when the function.py file is in the same folder as the program.
#import functions it's used as functions.get_todos()
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("Welcome!")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action.lower()  # Convert the input to lowercase
    user_action.strip()  # Remove leading and trailing whitespaces

    if user_action.startswith("add"):
        todo = user_action[4:]

        # Open a file in read mode
        todos = get_todos()

        # Add an item to the end of the list
        todos.append(todo + '\n')

        # Open a file in write mode
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter the new to-do: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid, babe. Try again. ")
            continue

    elif user_action.startswith("complete"):
        number = int(user_action[9:])

        todos = get_todos()

        index = number - 1
        todo_to_remove = todos[index].strip('\n') # strip.('\n') removes the break-line from that to-to item
        todos.pop(index) # .pop(index) removes the item with said {index}

        write_todos(todos)

        msg = f"The item called '{todo_to_remove}' was removed from the list."
        print(msg)

    elif user_action.startswith("exit"):
        break

    else:  # Default case for invalid inputs
            print("Invalid input. Please try again.")


print("Bye!")