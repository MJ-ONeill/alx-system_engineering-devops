#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress"""

import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
            .format(userId))

    EMPLOYEE_NAME = user.json().get('EMPLOYEE_NAME')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            TOTAL_NUMBER_OF_TASKS += 1
            if task.get('NUMBER_OF_DONE_TASKS'):
                NUMBER_OF_DONE_TASKS += 1

    print('Employee {} is done with tasks({}/{}):'.format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
        if task.get('userId') == int(userId) and task.get('NUMBER_OF_DONE_TASKS')]))
