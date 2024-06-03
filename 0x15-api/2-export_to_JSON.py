#!/usr/bin/python3
"""
Python script that uses REST API, for a given ID, returns information
in the JSON format.
"""
import json
import requests
import sys

if __name__ == '__main__':

    BASE_URL = 'https://jsonplaceholder.typicode.com'

    if len(sys.argv) < 2:
        print('Please provide an employee ID as an argument.')
        sys.exit(1)

    employee_id = int(sys.argv[1])

    response = requests.get('{}/todos?userId={}'.format(
        BASE_URL, employee_id))

    todos = response.json()

    total_tasks = len(todos)

    completed_tasks = sum(1 for todo in todos if todo['completed'])

    user_id = todos[0]['userId']
    response = requests.get('{}/users/{}'.format(BASE_URL, user_id))
    employee = response.json()
    employee_name = employee['username']

    tasks = []
    for todo in todos:
        task = {}
        task['task'] = todo['title']
        task['completed'] = todo['completed']
        task['username'] = employee_name
        tasks.append(task)

    user_tasks = {}
    user_tasks[str(user_id)] = tasks

    filename = '{}.json'.format(user_id)
    with open(filename, 'w') as f:
        json.dump(user_tasks, f)
