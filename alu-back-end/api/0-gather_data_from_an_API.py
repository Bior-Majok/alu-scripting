#!/usr/bin/python3
"""
Fetches and displays TODO list progress for a given employee
using only built-in urllib (no requests module).
"""

import urllib.request
import json
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Build URLs
    user_url = "{}/users/{}".format(base_url, emp_id)
    todos_url = "{}/todos?userId={}".format(base_url, emp_id)

    # Fetch user data
    with urllib.request.urlopen(user_url) as response:
        user_data = json.loads(response.read().decode())

    # Fetch todos data
    with urllib.request.urlopen(todos_url) as response:
        todos_data = json.loads(response.read().decode())

    emp_name = user_data.get("name")
    completed = [t for t in todos_data if t.get("completed")]
    total = len(todos_data)
    done = len(completed)

    print("Employee {} is done with tasks({}/{}):".format(emp_name, done, total))
    for task in completed:
        print("\t {}".format(task.get("title")))

