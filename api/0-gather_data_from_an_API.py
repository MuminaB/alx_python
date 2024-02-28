# import requests
# import sys

# def get_employee_todo_progress(employee_id):
#     # Fetch employee details
#     employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
#     employee = employee_response.json()

#     # Fetch employee's TODOs
#     todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
#     todos = todos_response.json()

#     # Calculate TODO progress
#     total_tasks = len(todos)
#     done_tasks = len([todo for todo in todos if todo['completed']])
#     done_task_titles = [todo['title'] for todo in todos if todo['completed']]

#     # Display TODO progress
#     print(f'Employee {employee["name"]} is done with tasks({done_tasks}/{total_tasks}):')
#     for title in done_task_titles:
#         print(f'\t {title}')

# if __name__ == "__main__":
#     get_employee_todo_progress(int(sys.argv[1]))

import requests

def get_employee_todo_progress(employee_id):
  """
  Retrieves and displays the TODO list progress of a given employee.

  Args:
    employee_id: The integer ID of the employee.

  Raises:
    ValueError: If the employee ID is not a positive integer.
  """

  # Validate input
  if not isinstance(employee_id, int) or employee_id <= 0:
    raise ValueError("Employee ID must be a positive integer.")

  # Build API endpoints for details and TODOs
  details_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
  todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

  # Fetch employee details
  try:
    response = requests.get(details_url)
    response.raise_for_status()  # Raise exception for non-200 status codes
    employee_data = response.json()
    employee_name = employee_data["name"]
  except requests.exceptions.RequestException as e:
    print(f"Error fetching employee details: {e}")
    return

  # Fetch TODOs
  try:
    response = requests.get(todos_url)
    response.raise_for_status()
    todos = response.json()
  except requests.exceptions.RequestException as e:
    print(f"Error fetching TODOs: {e}")
    return

  # Calculate completed tasks
  completed_tasks = sum(todo["completed"] for todo in todos)
  total_tasks = len(todos)

  # Display progress in the required format
  print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
  for todo in todos:
    if todo["completed"]:
      print(f"\t {todo['title']}")

if __name__ == "__main__":
  # Get employee ID from user input (replace with error handling if needed)
  employee_id = int(input("Enter employee ID: "))

  # Call the function
  get_employee_todo_progress(employee_id)
 
  
