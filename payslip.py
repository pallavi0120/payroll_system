# payslip.py

class PayslipGenerator:
    @staticmethod
    def generate(payroll_data: dict) -> str:
        payslip = f"""
==================================================
              PAYSLIP / SALARY STATEMENT          
==================================================
Employee ID   : {payroll_data['emp_id']}
Employee Name : {payroll_data['name']}
Department    : {payroll_data['department']}
--------------------------------------------------
EARNINGS                          AMOUNT (₹)
--------------------------------------------------
Gross Salary                     {payroll_data['gross_salary']:,.2f}
--------------------------------------------------
DEDUCTIONS                        AMOUNT (₹)
--------------------------------------------------
Provident Fund (PF)              {payroll_data['pf']:,.2f}
Professional Tax (PT)            {payroll_data['pt']:,.2f}
TDS (Income Tax)                 {payroll_data['tds']:,.2f}
Leave Deduction (LWP)            {payroll_data['lwp_deduction']:,.2f}
--------------------------------------------------
Total Deductions                 {payroll_data['total_deductions']:,.2f}
==================================================
NET PAYABLE SALARY               ₹{payroll_data['net_salary']:,.2f}
==================================================
"""
        return payslip