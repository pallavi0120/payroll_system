# database.py
import sqlite3
from models import Employee

class DatabaseManager:
    def __init__(self, db_name="payroll.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                emp_id TEXT PRIMARY KEY,
                name TEXT,
                department TEXT,
                basic_salary REAL
            )
        """)
        self.conn.commit()

    def save_employee(self, employee: Employee):
        self.cursor.execute("""
            INSERT OR REPLACE INTO employees (emp_id, name, department, basic_salary)
            VALUES (?, ?, ?, ?)
        """, (employee.emp_id, employee.name, employee.department, employee.basic_salary))
        self.conn.commit()

    def get_employee(self, emp_id: str) -> Employee:
        self.cursor.execute("SELECT emp_id, name, department, basic_salary FROM employees WHERE emp_id = ?", (emp_id,))
        row = self.cursor.fetchone()
        if row:
            return Employee(emp_id=row[0], name=row[1], department=row[2], basic_salary=row[3])
        return None

    def close(self):
        self.conn.close()