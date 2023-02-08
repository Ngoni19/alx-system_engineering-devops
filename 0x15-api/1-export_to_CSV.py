#!/usr/bin/python3
"""
Script requests from API then Return TODO list progress given the employee ID
Export the data to CSV file
"""
import csv
import requests
from sys import argv


def to_csv():
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

    """export the data to csv from API"""
    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for tk in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": tk[0],
                             "TASK_TITLE": tk[1]})


if __name__ == "__main__":
    to_csv()
