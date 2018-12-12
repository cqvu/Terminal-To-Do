""" Test functions for todo_module"""

from todo_module import *

def test_do():
    clear() # Make sure the file is empty

    # Test Case 1: Adding one task
    do("Test the do function")
    with open('todo_file.txt', 'r') as read_file:
        list = read_file.readlines()

    assert len(list) == 1
    assert list[0] == "Test the do function\n"

    # Test Case 2: Adding multiple tasks
    do("Test the do function again")
    do("Test the do function three times")
    with open('todo_file.txt', 'r') as read_file:
        list = read_file.readlines()

    assert len(list) == 3
    assert list[1] == "Test the do function again\n"
    assert list[2] == "Test the do function three times\n"

    clear()

def test_delete():
    clear() # Make sure the file is empty

    # Populate the todo_file
    for num in range(0,10):
        do("task" + str(num))

    # Test Case 1: Delete top of list
    deleted = delete(0)
    with open('todo_file.txt', 'r') as read_file:
        list = read_file.readlines()

    assert isinstance(deleted, str)
    assert len(list) == 9
    assert list[0] != deleted

    # Test Case 2: Delete end of list
    deleted = delete(8)
    with open('todo_file.txt', 'r') as read_file:
        list = read_file.readlines()

    assert isinstance(deleted, str)
    assert len(list) == 8

    # Test Case 3: Delete middle of list
    deleted = delete(4)
    deleted2 = delete(2)
    with open('todo_file.txt', 'r') as read_file:
        list = read_file.readlines()

    assert isinstance(deleted, str)
    assert isinstance(deleted2, str)
    assert len(list) == 6

    clear()

def test_done():
    clear_all() # Make sure the file is empty

    # Populate the todo_file
    for num in range(0,10):
        do("task" + str(num))

    task_done = done(5)
    task2_done = done(2)
    with open('todo_file.txt', 'r') as read_file:
        list = read_file.readlines()

    with open('done_file.txt', 'r') as done_file:
        done_list = done_file.readlines()

    assert isinstance(task_done, str)
    assert isinstance(task2_done, str)
    assert len(list) == 8
    assert len(done_list) == 2
    assert done_list[0] == task_done
    assert done_list[1] == task2_done


def test_clear():
    # Populate the todo_file
    for num in range(0,10):
        do("task" + str(num))

    clear()
    with open('todo_file.txt', 'r') as read_file:
        list = read_file.readlines()

    assert len(list) == 0

def test_clear_all():
    # Populate the todo_file
    for num in range(0,10):
        do("task" + str(num))

    # Populate the done_file
    for num in range(2,5):
        done(num)

    clear_all()

    with open('todo_file.txt', 'r') as read_file:
        list = read_file.readlines()
    with open('done_file.txt', 'r') as done_file:
        done_list = done_file.readlines()

    assert len(list) == 0
    assert len(done_list) == 0
