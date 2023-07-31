#!/usr/bin/python3
"""
Write a Python script using REST API to gather employee data"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + "users/{}".format(sys.argv[1])
    todo_url = url + "todos"
    params = {"userId": sys.argv[1]}
    user = requests.get(url=user_url).json()
    todos = requests.get(url=todo_url, params=params).json()
    completed = sum(1 for todo in todos if todo.get("completed"))

    print("Employee {} is done with tasks ({}/{}):".format(
        user.get("name"), completed, len(todos)))

    for todo in todos:
        if todo.get("completed") is True:
            print("\t{}".format(todo.get("TASK_TITLE)))
