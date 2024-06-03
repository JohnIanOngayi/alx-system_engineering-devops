#!/usr/bin/python3
"""
Python script that, uses REST API, for all employees,
returns information in a raw dict
"""
import json
import requests


if __name__ == '__main__':
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    response = requests.get('{}/users'.format(BASE_URL))
    users = response.json()

    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        response = requests.get('{}/todos?userId={}'.format(
            BASE_URL, user_id))
        todos = response.json()

        user_tasks = []
        for todo in todos:
            task = {'username': username,
                    'task': todo['title'],
                    'completed': todo['completed']}
            user_tasks.append(task)

        all_tasks[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file, indent=4)
