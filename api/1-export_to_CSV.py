import csv
import requests
import sys

def export_employee_todo_to_csv(employee_id):
    """
    Retrieves TODO list progress for a given employee ID using the REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None: Displays the employee's TODO list progress in the specified format.
    """
   
    # Fetch employee details
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee = employee_response.json()

    # Fetch employee's TODOs
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todos = todos_response.json()

    # Prepare data for CSV
    data_for_csv = []
    for todo in todos:
        data_for_csv.append([employee["id"], employee["username"], todo['completed'], todo['title']])

    # Write data to CSV
    with open(f'{employee_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(data_for_csv)

    print(f'Data exported to {employee_id}.csv')

if __name__ == "__main__":
    get_employee_todo_progress(int(sys.argv[1]))
