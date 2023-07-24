#!/usr/bin/python3
"""
Write a Python script using REST API to gather employe data"""
import requests
import sys

if __name__ == "main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + "users/{}".format(sys.argv[1])
    todo_url = url + "todos"
    params = {"user_ID: sys.arv[1]"}
    user = requests.get(url=user_url).json()
    todos = requests.get(url=todo_url, paramas=params).json()
    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

        print("Employee {} is done with tasks({}/{}):"
              .format(user.get("name"), len(completed), len(todos)))

        for complete in completed:
            print("\t {}".format(complete))
