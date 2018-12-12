""" Functions that perform the basic features of a todo-list"""

def do(task):
    with open('todo_file.txt', 'a+') as write_file:
        write_file.write(task + "\n")
    print("%s added to TODO" % task)
    view_todo()

def done(index):
    task = delete(index)

    with open('done_file.txt', 'a+') as write_file:
        write_file.write(task)

    print("%s completed, great job!" % task.rstrip('\n'))
    return task

def delete(index):
    with open('todo_file.txt', 'r') as read_file:
        list = read_file.readlines()

    index = (int)(index)
    task = list[index]
    del list[index]

    # Update todo_file
    with open('todo_file.txt', 'w') as write_file:
        for item in list:
            write_file.write(item)

    view_todo()
    print("%s deleted." % task.rstrip('\n'))
    return task

def view_todo():
    with open('todo_file.txt', 'r') as read_file:
        list = read_file.readlines()
    print("\n")
    for index, item in enumerate(list):
        print("[%d] %s" % (index, item))
    print("\n")

def view_done():
    with open('done_file.txt', 'r') as read_file:
        list = read_file.readlines()
    print("\n")
    for index, item in enumerate(list):
        print("[%d] %s" % (index, item))
    print("\n")

def clear():
    open('todo_file.txt', 'w').close()
    print("To-do list cleared.")

def clear_all():
    open('todo_file.txt', 'w').close()
    open('done_file.txt', 'w').close()
    print("To-do list cleared.")
    print("Done list cleared.")
