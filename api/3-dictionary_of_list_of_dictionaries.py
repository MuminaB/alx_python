import json
import requests

def export_all_employee_todo_to_json():
    # Fetch all employee details
    all_employee_response = requests.get('https://jsonplaceholder.typicode.com/users')
    all_employees = all_employee_response.json()

    data = {}

    for employee in all_employees:
        employee_id = employee["id"]

        # Fetch employee's TODOs
        todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
        todos = todos_response.json()

        # Prepare data for JSON
        data[employee_id] = []
        for todo in todos:
            data[employee_id].append({
                "task": todo['title'],
                "completed": todo['completed'],
                "username": employee["username"]
            })

    # Write data to JSON
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    export_all_employee_todo_to_json()
 