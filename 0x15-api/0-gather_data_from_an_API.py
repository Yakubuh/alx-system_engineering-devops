#!/usr/bin/python3
"""ejercicio 1"""
import requests
from sys import argv


def API_request(args):
    """API"""
    t = "https://jsonplaceholder.typicode.com/todos/?userId=" + str(argv[1])
    users = "https://jsonplaceholder.typicode.com/users/" + str(argv[1])

    response_todos = requests.get(t)
    response_users = requests.get(users)
    dic_t = response_todos.json()
    dic_u = response_users.json()
    name_user = dic_u.get("name")
    count_total = 0
    count_true = 0
    list_carlitos = []
    for tasks in dic_t:
        count_total += 1
        if tasks.get('completed') is True:
            list_carlitos.append(tasks)
            count_true += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name_user, count_true, count_total))
    for task in list_carlitos:
        print("\t " "{}".format(task.get('title')))

if __name__ == "__main__":
    API_request(argv)
