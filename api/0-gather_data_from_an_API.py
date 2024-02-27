# import requests

# def get_employee_todo_progress(employee_id):
#     base_url = "https://jsonplaceholder.typicode.com"
#     user_endpoint = f"{base_url}/users/{employee_id}"
#     todos_endpoint = f"{base_url}/users/{employee_id}/todos"

#     try:
#         user_response = requests.get(user_endpoint)
#         user_data = user_response.json()
#         employee_name = user_data["name"]

#         todos_response = requests.get(todos_endpoint)
#         todos_data = todos_response.json()

#         total_tasks = len(todos_data)
#         done_tasks = sum(1 for todo in todos_data if todo["completed"])

#         print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
#         for todo in todos_data:
#             if todo["completed"]:
#                 print(f"\t{todo['title']}")

#     except requests.RequestException as e:
#         print(f"Error fetching data: {e}")

# if __name__ == "__main__":
#     employee_id = int(input("Enter the employee ID: "))
#     get_employee_todo_progress(employee_id)
<<<<<<< HEAD
=======
   
>>>>>>> 0fc902a (try again)

import requests
import sys

def get_employee_todo_progress(employee_id):
    # Fetch employee details
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee = employee_response.json()

    # Fetch employee's TODOs
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todos = todos_response.json()

    # Calculate TODO progress
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo['completed']])
    done_task_titles = [todo['title'] for todo in todos if todo['completed']]

    # Display TODO progress
    print(f'Employee {employee["name"]} is done with tasks({done_tasks}/{total_tasks}):')
    for title in done_task_titles:
        print(f'\t {title}')

if __name__ == "__main__":
    get_employee_todo_progress(int(sys.argv[1]))
<<<<<<< HEAD
  
=======
 
>>>>>>> 0fc902a (try again)
