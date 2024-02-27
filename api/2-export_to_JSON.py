import json
import requests
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import sys
=======
import csv
>>>>>>> 4858c15 (gh)
=======
>>>>>>> 0548cc1 (try)

<<<<<<< HEAD
def export_employee_todo_to_json(employee_id):
    """
    Retrieves todo list progress for a given employee ID using the REST API.
=======
def get_employee_todo_progress(employee_id):
=======
import sys

def export_employee_todo_to_json(employee_id):
>>>>>>> 47515b6 (commit)
=======

def get_employee_todo_progress(employee_id):
>>>>>>> 937f9e1 (m)
    """
    Retrieves todo list progress for a given employee ID using the REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None: Displays the employee's todo list progress in the specified format.
    """
<<<<<<< HEAD
<<<<<<< HEAD
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

<<<<<<< HEAD
<<<<<<< HEAD
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
=======
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for todo in todos_data:
                writer.writerow([employee_id, employee_name, todo["completed"], todo["title"]])
=======
        json_output = {
            str(employee_id): [
                {
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": employee_name
                }
                for todo in todos_data
            ]
        }
>>>>>>> 0548cc1 (try)

        json_filename = f"{employee_id}.json"
        with open(json_filename, "w") as json_file:
            json.dump(json_output, json_file, indent=4)

        print(f"JSON file '{json_filename}' created successfully!")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
<<<<<<< HEAD
  
>>>>>>> 4858c15 (gh)
=======
   
>>>>>>> 0548cc1 (try)
=======
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee = employee_response.json()
=======
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/users/{employee_id}/todos"
>>>>>>> 937f9e1 (m)

    try:
        user_response = requests.get(user_endpoint)
        user_data = user_response.json()
        employee_name = user_data["name"]

        todos_response = requests.get(todos_endpoint)
        todos_data = todos_response.json()

        json_output = {
            str(employee_id): [
                {
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": employee_name
                }
                for todo in todos_data
            ]
        }

        json_filename = f"{employee_id}.json"
        with open(json_filename, "w") as json_file:
            json.dump(json_output, json_file, indent=4)

        print(f"JSON file '{json_filename}' created successfully!")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
<<<<<<< HEAD
    export_employee_todo_to_json(int(sys.argv[1]))
>>>>>>> 47515b6 (commit)
=======
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
   
>>>>>>> 937f9e1 (m)
