#!/usr/bin/python3
"""Ejercicio 2"""
import csv
import requests
from sys import argv


def export_csv(args):
    """Export csv"""
    t = "https://jsonplaceholder.typicode.com/todos/?userId=" + str(argv[1])
    users = "https://jsonplaceholder.typicode.com/users/" + str(argv[1])

    response_todos = requests.get(t)
    response_users = requests.get(users)
    dic_t = response_todos.json()
    dic_u = response_users.json()
    name_user = dic_u.get("username")

    with open(str(argv[1] + ".csv"), mode='w') as f:
        my_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for count in dic_t:
            my_writer.writerow([str(argv[1]), str(name_user),
                                str(count['completed']), (count['title'])])
if __name__ == "__main__":
    export_csv(argv)
