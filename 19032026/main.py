# sort dictionary with lambda
employees = [
    {"name": "A", "salary": 50}, 
    {"name": "B", "salary": 70}, 
    {"name": "C", "salary": 60}
]

sorted_employees = sorted(employees, key=lambda x: x['salary'], reverse=True)
for emp in sorted_employees:
    print(emp)