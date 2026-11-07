# app.py
import streamlit as st
from models import Employee
from payroll import PayrollProcessor
from payslip import PayslipGenerator
from database import DatabaseManager

# Page configuration
st.set_page_config(page_title="Payroll Management System", page_icon="💼", layout="centered")

# Initialize database
db = DatabaseManager()

st.title("💼 Employee Payroll Management System")
st.markdown("Manage employee records, compute statutory deductions, and generate payslips instantly.")

# --- SIDEBAR: REGISTER OR UPDATE EMPLOYEE ---
st.sidebar.header("👤 Employee Management")
with st.sidebar.form("emp_form"):
    emp_id = st.text_input("Employee ID", value="EMP101")
    name = st.text_input("Employee Name", value="Pallavi Sharma")
    department = st.text_input("Department", value="Engineering")
    basic_salary = st.number_input("Basic Salary (₹)", value=45000.0, step=1000.0)
    
    submitted = st.form_submit_button("Save Employee to DB")
    if submitted:
        emp = Employee(emp_id, name, department, basic_salary)
        db.save_employee(emp)
        st.sidebar.success(f"Successfully saved {name}!")

# --- MAIN AREA: PAYROLL COMPUTATION ---
st.header("⚙️ Payroll Processing & Payslip Generator")

# Fetch all registered employees from SQLite
db.cursor.execute("SELECT emp_id, name FROM employees")
rows = db.cursor.fetchall()

if rows:
    emp_dict = {f"{row[0]} - {row[1]}": row[0] for row in rows}
    selected_label = st.selectbox("Select Employee", list(emp_dict.keys()))
    selected_emp_id = emp_dict[selected_label]
    
    # Retrieve full employee details
    emp_obj = db.get_employee(selected_emp_id)
    
    col1, col2 = st.columns(2)
    with col1:
        lwp_days = st.number_input("Leave Without Pay (LWP) Days", min_value=0, max_value=30, value=2)
    with col2:
        total_working_days = st.number_input("Total Working Days in Month", min_value=1, max_value=31, value=30)
        
    if st.button("Compute Salary & Generate Payslip", type="primary"):
        payroll_result = PayrollProcessor.compute_payroll(emp_obj, lwp_days=lwp_days, total_working_days=total_working_days)
        payslip_output = PayslipGenerator.generate(payroll_result)
        
        st.subheader("📄 Generated Payslip")
        st.text(payslip_output)
        
        # Download button for the payslip text file
        st.download_button(
            label="📥 Download Payslip as Text File",
            data=payslip_output,
            file_name=f"payslip_{emp_obj.emp_id}.txt",
            mime="text/plain"
        )
else:
    st.info("No employees found in the database. Use the sidebar to add your first employee.")