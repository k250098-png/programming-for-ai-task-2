
employees = {
    "E101": {"name": "Ali", "department": "IT", "salary": 85000, "job_title": "Developer"},
    "E102": {"name": "Sara", "department": "HR", "salary": 75000, "job_title": "HR Specialist"},
    "E103": {"name": "Ahmed", "department": "IT", "salary": 95000, "job_title": "Manager"}
}


def search_employee(emp_id):
    return employees.get(emp_id, "Employee not found")

def add_employee(emp_id, name, department, salary, job_title):
    if emp_id in employees:
        print(f"Employee ID {emp_id} already exists.")
    else:
        employees[emp_id] = {
            "name": name,
            "department": department,
            "salary": salary,
            "job_title": job_title
        }
        print(f"Added employee: {name} ({emp_id})")


def update_salary(emp_id, new_salary):
    if emp_id in employees:
        employees[emp_id]["salary"] = new_salary
        print(f"Updated salary for {emp_id} to ${new_salary}")
    else:
        print("Employee not found.")


def remove_employee(emp_id):
    if emp_id in employees:
        removed = employees.pop(emp_id)
        print(f"Removed employee: {removed['name']} ({emp_id})")
    else:
        print("Employee not found.")


print("--- Search Employee ---")
print("Search E102:", search_employee("E102"))

print("\n--- Add Employee ---")
add_employee("E104", "Zain", "Finance", 90000, "Analyst")

print("\n--- Update Salary ---")
update_salary("E101", 90000)

print("\n--- Remove Employee ---")
remove_employee("E102")
