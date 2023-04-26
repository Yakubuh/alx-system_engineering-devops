#!/usr/bin/python3
"""task"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    def Requests_API(argv):
        """Requests_API"""
    req_all = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId="+str(argv[1]))
    req_user = requests.get(
        "https://jsonplaceholder.typicode.com/users/"+str(argv[1]))

    user_name = req_user.json().get("username")
    # instance of json representation
    json_all = req_all.json()

    dic_ppl = {}
    lis_json = []
    # dic = {'task': '', 'completed': None, 'username': user_name}
    for i in json_all:
        dic = {'task': '', 'completed': None, 'username': user_name}
        task_title = i.get('title')
        compl = i.get('completed')
        dic.update(task=task_title, completed=compl)
        lis_json.append(dic)
    dic_ppl.update({argv[1]: lis_json})

    with open('{}.json'.format(argv[1]), 'w', encoding='utf-8') as f:
        json.dump(dic_ppl, f)
