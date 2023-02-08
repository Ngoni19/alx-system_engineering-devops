#!/usr/bin/python3
"""
Script requests from API then Return TODO list progress given the employee ID
Export the data to JSON
"""
from sys import argv
import json
import requests


def to_json():
    """return the API data here"""
    Users = requests.get("http://jsonplaceholder.typicode.com/users")
    for p in Users.json():
        if p.get('id') == int(argv[1]):
            USERNAME = (p.get('username'))
            break
    TASK_STATUS_TITLE = []
    to_do = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in to_do.json():
        if t.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    """Export data to json"""
    t = []
    for tk in TASK_STATUS_TITLE:
        t.append({"task": tk[1], "completed": tk[0], "username": USERNAME})
    Data = {str(argv[1]): t}
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as F:
        json.dump(Data, F)


if __name__ == "__main__":
    to_json()
