import json
import requests

def get_all_employees_todo_progress():
    """
    Retrieves TODO list progress for all employees using the REST API.

    Returns:
        None: Displays the employee TODO list progress in the specified format.
    """
    base_url = "https://jsonplaceholder.typicode.com/users"

    try:
        users_response = requests.get(base_url)
        users_data = users_response.json()

        all_employees_tasks = {}

        for user in users_data:
            employee_id = user["id"]
            employee_name = user["name"]

            todos_endpoint = f"{base_url}/{employee_id}/todos"
            todos_response = requests.get(todos_endpoint)
            todos_data = todos_response.json()

            employee_tasks = [
                {
                    "username": employee_name,
                    "task": todo["title"],
                    "completed": todo["completed"]
                }
                for todo in todos_data
            ]

            all_employees_tasks[str(employee_id)] = employee_tasks

        json_filename = "todo_all_employees.json"
        with open(json_filename, "w") as json_file:
            json.dump(all_employees_tasks, json_file, indent=4)

        print(f"JSON file '{json_filename}' created successfully!")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    get_all_employees_todo_progress()
   