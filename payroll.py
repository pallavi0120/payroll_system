# payroll.py
from models import Employee

class PayrollProcessor:
    @staticmethod
    def compute_payroll(employee: Employee, lwp_days: int = 0, total_working_days: int = 30) -> dict:
        # Earnings calculation (typically structured around basic salary)
        basic = employee.basic_salary
        hra = basic * 0.40          # 40% HRA
        special_allowance = basic * 0.30 # 30% Special Allowance
        
        gross_salary = basic + hra + special_allowance
        
        # Loss of Pay (LWP) Adjustment
        per_day_salary = gross_salary / total_working_days if total_working_days > 0 else 0
        lwp_deduction = per_day_salary * lwp_days
        
        # Statutory Deductions
        pf = basic * 0.12           # 12% Provident Fund on Basic
        pt = 200.0                  # Standard Professional Tax slab
        tds = 1500.0 if gross_salary > 50000 else 500.0  # Estimated TDS slab
        
        total_deductions = pf + pt + tds + lwp_deduction
        net_salary = gross_salary - total_deductions
        
        return {
            "emp_id": employee.emp_id,
            "name": employee.name,
            "department": employee.department,
            "gross_salary": round(gross_salary, 2),
            "pf": round(pf, 2),
            "pt": pt,
            "tds": tds,
            "lwp_deduction": round(lwp_deduction, 2),
            "total_deductions": round(total_deductions, 2),
            "net_salary": round(net_salary, 2)
        }