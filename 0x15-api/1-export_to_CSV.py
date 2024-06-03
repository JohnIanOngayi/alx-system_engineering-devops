#!/usr/bin/python3
"""
Python script that, uses REST API, for a given ID, returns information
in the CSV format.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    BASE_URL = 'https://jsonplaceholder.typicode.com/'

    if len(sys.argv) < 2:
        print("Please provide an employee ID as an argument")
        sys.exit(1)
    employee_id = int(sys.argv[1])

    response = requests.get(
            BASE_URL + "users/{}".format(employee_id)).json()

    employee_name = response.get("username")
    todos = requests.get(
            BASE_URL + "todos", params={"userId": employee_id}).json()

    csv_filename = '{}.csv'.format(employee_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                    [employee_id, employee_name,
                        todo['completed'], todo['title']])
