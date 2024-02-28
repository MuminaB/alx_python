# import csv
# import requests
# import sys

# def export_employee_todo_to_csv(employee_id):
#     ""
#     Retrieves TODO list progress for a given employee ID using the REST API.

#     Args:
#         employee_id (int): The ID of the employee.

#     Returns:
#         None: Displays the employee's TODO list progress in the specified format.
#     """
   
#     # Fetch employee details
#     employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
#     employee = employee_response.json()

#     # Fetch employee's TODOs
#     todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
#     todos = todos_response.json()

#     # Prepare data for CSV
#     data_for_csv = []
#     for todo in todos:
#         data_for_csv.append([employee["id"], employee["username"], todo['completed'], todo['title']])

#     # Write data to CSV
#     with open(f'{employee_id}.csv', 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
#         writer.writerows(data_for_csv)

#     print(f'Data exported to {employee_id}.csv')

# if __name__ == "__main__":
#     get_employee_todo_progress(int(sys.argv[1]))

import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    """Retrieves and displays employee TODO progress, exporting data to CSV.

    Args:
        employee_id: The integer ID of the employee.

    Raises:
        ValueError: If the employee ID is not a positive integer.
    """

    if not isinstance(employee_id, int) or employee_id <= 0:
        raise ValueError("Employee ID must be a positive integer.")

    details_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        response = requests.get(details_url)
        response.raise_for_status()
        employee_data = response.json()
        employee_name = employee_data["name"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching employee details: {e}")
        return

    try:
        response = requests.get(todos_url)
        response.raise_for_status()
        todos = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching TODOs: {e}")
        return

    csv_data = []
    for todo in todos:
        if todo["userId"] == employee_id:
            csv_data.append([employee_id, employee_name, todo["completed"], todo["title"]])

    filename = f"{employee_id}.csv"

    try:
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            writer.writerows(csv_data)
        print(f"Data exported to {filename}")
    except OSError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])

    get_employee_todo_progress(employee_id)
  
   