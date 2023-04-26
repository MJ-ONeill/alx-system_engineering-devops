#!/usr/bin/python3
"""extend your Python script to export data in the JSON format.
"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + "users").json()
    with open("todo_all_employees.json", "w") as json_file:
        json.dump({user.get("id"): [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")
        }for todo in requests.get(url + "todos",
                                  params={"userId": user.get("id")}
                                  ).json()]for user in users}, json_file)
