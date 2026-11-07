# test_payroll.py
import unittest
from models import Employee
from payroll import PayrollProcessor

class TestPayrollSystem(unittest.TestCase):
    def test_zero_lwp_payroll(self):
        emp = Employee("EMP102", "Rahul", "IT", 40000)
        result = PayrollProcessor.compute_payroll(emp, lwp_days=0, total_working_days=30)
        self.assertEqual(result['gross_salary'], 68000.0)
        self.assertGreater(result['net_salary'], 0)

    def test_lwp_deduction(self):
        emp = Employee("EMP103", "Ananya", "HR", 50000)
        result_no_lwp = PayrollProcessor.compute_payroll(emp, lwp_days=0, total_working_days=30)
        result_with_lwp = PayrollProcessor.compute_payroll(emp, lwp_days=5, total_working_days=30)
        self.assertGreater(result_with_lwp['lwp_deduction'], 0)
        self.assertLess(result_with_lwp['net_salary'], result_no_lwp['net_salary'])

if __name__ == "__main__":
    unittest.main()