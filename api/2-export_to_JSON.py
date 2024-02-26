import json
import requests
import sys

<<<<<<< HEAD
def export_employee_todo_to_json(employee_id):
    """
    Retrieves todo list progress for a given employee ID using the REST API.
=======
def get_employee_todo_progress(employee_id):
    """
    Retrieves TODO list progress for a given employee ID using the REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None: Displays the employee's TODO list progress in the specified format.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/users/{employee_id}/todos"
>>>>>>> 965849c (docstring)

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None: Displays the employee's todo list progress in the specified format.
    """
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee = employee_response.json()

    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todos = todos_response.json()

    data = {employee_id: []}
    for todo in todos:
        data[employee_id].append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": employee["username"]
        })

    with open(f'{employee_id}.json', 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    export_employee_todo_to_json(int(sys.argv[1]))
