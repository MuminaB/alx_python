import requests
import csv

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/users/{employee_id}/todos"

    try:
        user_response = requests.get(user_endpoint)
        user_data = user_response.json()
        employee_name = user_data["name"]

        todos_response = requests.get(todos_endpoint)
        todos_data = todos_response.json()

        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for todo in todos_data:
                writer.writerow([employee_id, employee_name, todo["completed"], todo["title"]])

        print(f"CSV file '{csv_filename}' created successfully!")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
  