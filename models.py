# models.py

class Employee:
    def __init__(self, emp_id: str, name: str, department: str, basic_salary: float):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.basic_salary = basic_salary