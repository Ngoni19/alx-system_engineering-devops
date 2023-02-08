#!/usr/bin/python3
"""
Script requests from API then Return TODO list progress given the employee ID
"""
from sys import argv
import requests


def display():
    """return the API data here"""
    Users = requests.get("http://jsonplaceholder.typicode.com/users")
    for p in Users.json():
        if p.get('id') == int(argv[1]):
            EMPLOYEE_NAME = (p.get('name'))
            break
    TOTAL_NUM_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    to_do = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in to_do.json():
        if t.get('userId') == int(argv[1]):
            TOTAL_NUM_OF_TASKS += 1
            if t.get('completed') is True:
                    NUMBER_OF_DONE_TASKS += 1
                    TASK_TITLE.append(t.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    for tk in TASK_TITLE:
        print("\t {}".format(tk))


if __name__ == "__main__":
    display()
