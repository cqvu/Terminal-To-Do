""" Functions that perform the basic features of a todo-list"""

""" Add a task to the todo list.

    Parameters
    ----------
    task : str
        The task to be added.
    """
def do(task):
    with open('todo_file.txt', 'a+') as write_file:
        write_file.write(task + "\n")
    print("%s added to TODO" % task)
    view_todo()

""" Mark a task completed by removing it from the todo list
    and adding it to the done list.

    Parameters
    ----------
    index : int
        The index of the task to be marked completed

    Returns
    ----------
    task : str
        The task marked completed.
    """
def done(index):
    task = delete(index)

    with open('done_file.txt', 'a+') as write_file:
        write_file.write(task)

    print("%s completed, great job!" % task.rstrip('\n'))
    return task

""" Remove a task from the todo list.

    Parameters
    ----------
    index : int
        The index of the task to be deleted.

    Returns
    ----------
    task : str
        The task deleted.
    """
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

    print("%s deleted." % task.rstrip('\n'))
    view_todo()
    return task

""" Print out the current todo list."""
def view_todo():
    with open('todo_file.txt', 'r') as read_file:
        list = read_file.readlines()
    print("\nTODO: \n")
    # Print the todo list in the format: [index] task
    for index, item in enumerate(list):
        print("[%d] %s" % (index, item))
    print("\n")

""" Print out the accomplishment list."""
def view_done():
    with open('done_file.txt', 'r') as read_file:
        list = read_file.readlines()
    print("\nACCOMPLISHED: \n ")
    for index, item in enumerate(list):
        print("[%d] %s" % (index, item))
    print("\n")

""" Erase all data from todo list."""
def clear():
    open('todo_file.txt', 'w').close()
    print("To-do list cleared.")

""" Erase all data from todo and done lists."""
def clear_all():
    open('todo_file.txt', 'w').close()
    open('done_file.txt', 'w').close()
    print("To-do list cleared.")
    print("Done list cleared.")
