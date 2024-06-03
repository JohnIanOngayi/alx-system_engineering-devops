#!/usr/bin/python3
"""
Python script that, uses REST API, for a given
employee ID, returns information about his/her TODO
list progress.
"""
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
    employee_name = employee['name']

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_tasks, total_tasks))

    for todo in todos:
        if todo['completed']:
            print('\t {}'.format(todo['title']))
