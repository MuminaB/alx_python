import json
import requests

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
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
   
