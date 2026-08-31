
employees = [
    ("E101", "Ali", "IT", 85000),
    ("E102", "Sara", "HR", 75000),
    ("E103", "Ahmed", "IT", 95000),
    ("E104", "Zain", "Finance", 90000)
]


emp_lookup = {
    emp[0]: {"name": emp[1], "department": emp[2], "salary": emp[3]} 
    for emp in employees
}


it_employees = [
    info["name"] for info in emp_lookup.values() if info["department"] == "IT"
]


total_salary = sum(info["salary"] for info in emp_lookup.values())
avg_salary = total_salary / len(emp_lookup)


highest_paid_id = max(emp_lookup, key=lambda emp_id: emp_lookup[emp_id]["salary"])
highest_paid = emp_lookup[highest_paid_id]

unique_departments = {info["department"] for info in emp_lookup.values()}


dept_counts = {}
for info in emp_lookup.values():
    dept = info["department"]
    dept_counts[dept] = dept_counts.get(dept, 0) + 1


def get_employee_by_id(emp_id):
    return emp_lookup.get(emp_id, "Employee not found")

print("--- Employee Analysis Results ---")
print("1. IT Department Employees:", it_employees)
print(f"2. Average Salary: ${avg_salary:.2f}")
print(f"3. Highest Salary: {highest_paid['name']} (${highest_paid['salary']})")
print("4. Existing Departments:", unique_departments)
print("5. Department Counts:", dept_counts)
print("\n--- Direct ID Lookup Test ---")
print("Lookup 'E103':", get_employee_by_id("E103"))
