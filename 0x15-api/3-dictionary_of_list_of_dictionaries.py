#!/usr/bin/python3
"""
Script requests from API then Return TODO list progress given the employee ID
Export data to JSON
"""
import json
import requests


def all_to_json():
    """return the API data here"""
    Users = []
    _Users = requests.get("http://jsonplaceholder.typicode.com/users")
    for p in _Users.json():
        Users.append((p.get('id'), p.get('username')))
    TASK_STATUS_TITLE = []
    to_do = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in to_do.json():
        TASK_STATUS_TITLE.append((t.get('userId'),
                                  t.get('completed'),
                                  t.get('title')))

    """export data to json"""
    Data = dict()
    for p in Users:
        t = []
        for tk in TASK_STATUS_TITLE:
            if tk[0] == p[0]:
                t.append({"task": tk[2], "completed": tk[1],
                          "username": p[1]})
        Data[str(p[0])] = t
    filename = "todo_all_employees.json"
    with open(filename, "w") as F:
        json.dump(Data, F, sort_keys=True)


if __name__ == "__main__":
    all_to_json()
