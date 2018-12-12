import datetime
from sys import argv
from todo_module import *

dt = datetime.datetime.now()
print("It is " + dt.strftime("%c") + "\n")
print("Welcome to Terminal To Do! Type 'help' to see usage instructions.\n")

view_todo()

user_input = input("What would you like to do? ")

while user_input != "quit":
    # Parse the command line arguments
    input_list = user_input.split()
    try:
        action = input_list[0]
    except:
        user_input = input("> ")
        continue
    arg = ""
    for item in input_list[1:]:
        arg += item + " "

    if(action == "help"):
        print('''
        Terminal To Do is your personal todo list right in the terminal!

        Usage:

            do [task] -- add a task

            done [number] -- complete a task

            delete [number] -- delete a task

            todo -- view the todo list

            todone -- view the done list

            clear -- clear todo list

            clear all -- clear todo and done lists

            quit -- exit the program

        Enjoy and stay productive!

        ''')

    elif action == "do":
        if(arg == ""):
            print("Please specify the task")
            user_input = input("> ")
            continue
        do(arg)

    elif action == "done":
        if(arg == ""):
            print("Please specify the number of the task")
            user_input = input("> ")
            continue
        done(arg)

    elif action == "delete":
        if(arg == ""):
            print("Please specify the number of the task")
            user_input = input("> ")
            continue
        delete(arg)

    elif action == "todo":
        view_todo()

    elif action == "todone":
        view_done()

    elif action == "clear":
        if(arg != ""):
            confirm = input("Clear todo and done lists? [y/n] ")
            if(confirm == "y"):
                clear_all()
        else:
            confirm = input("Clear todo list? [y/n] ")
            if(confirm == "y"):
                clear()

    else:
        print("Command not recognized, type 'help' to see usage instructions\n")

    user_input = input("> ")
