# main.py
from models import Employee
from payroll import PayrollProcessor
from payslip import PayslipGenerator
from database import DatabaseManager

def main():
    # 1. Initialize database manager
    db = DatabaseManager()

    # 2. Register or update employee in the database
    emp = Employee(emp_id="EMP101", name="Pallavi Sharma", department="Engineering", basic_salary=45000)
    db.save_employee(emp)

    # 3. Retrieve employee from database for payroll processing
    fetched_emp = db.get_employee("EMP101")
    
    if fetched_emp:
        # 4. Compute payroll with 2 days of LWP
        payroll_result = PayrollProcessor.compute_payroll(fetched_emp, lwp_days=2, total_working_days=30)
        
        # 5. Generate and print payslip
        print(PayslipGenerator.generate(payroll_result))
    
    db.close()

if __name__ == "__main__":
    main()