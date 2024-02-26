import csv
import requests
<<<<<<< HEAD
import sys

def export_employee_todo_to_csv(employee_id):
    """
    Retrieves TODO list progress for a given employee ID using the REST API.
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
>>>>>>> 0548cc1 (try)

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None: Displays the employee's TODO list progress in the specified format.
    """
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee = employee_response.json()

    # Fetch employee's TODOs
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todos = todos_response.json()

<<<<<<< HEAD
    # Prepare data for CSV
    data = []
    for todo in todos:
        data.append([employee_id, employee["username"], todo['completed'], todo['title']])
=======
        print(f"{csv_filename} created successfully!")
>>>>>>> 0548cc1 (try)

    # Write data to CSV
    with open(f'{employee_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)

if __name__ == "__main__":
    export_employee_todo_to_csv(int(sys.argv[1]))
 
