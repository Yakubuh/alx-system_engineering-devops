#!/usr/bin/python3
"""ejercicio 2"""
import json
import requests
from sys import argv


def export_json(args):
    """Export to JSON"""
    t = "https://jsonplaceholder.typicode.com/todos/?userId=" + str(argv[1])
    users = "https://jsonplaceholder.typicode.com/users/" + str(argv[1])

    response_todos = requests.get(t)
    response_users = requests.get(users)
    dic_t = response_todos.json()
    dic_u = response_users.json()
    name_user = dic_u.get("username")

    dict_ = {}
    list_j = []
    for count in dic_t:
        dictionary = {'task': '', 'completed': None, 'username': name_user}
        title_ = count.get('title')
        completed_ = count.get('completed')
        dictionary.update(task=title_, completed=completed_)
        list_j.append(dictionary)
    dict_.update({argv[1]: list_j})

    with open(str(argv[1] + ".json"), mode='w') as f:
        json.dump(dict_, f)


if __name__ == "__main__":
    export_json(argv)
