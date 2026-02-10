 # Sorting Employees

def sortEmployees(employee, salary):
    # Combine employee and salary
    data = list(zip(employee, salary))
    
    # Sort by salary first, then by name
    data.sort(key=lambda x: (x[1], x[0]))
    
    # Extract only employee names
    return [name for name, sal in data]

employee = ["chef", "geek"]
salary = [100, 50]

print(sortEmployees(employee, salary))
