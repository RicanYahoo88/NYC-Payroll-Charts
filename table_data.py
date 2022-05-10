from operator import index
from pickle import TRUE
import sqlite3
import pandas as pd

#connect to database
def get_conx():
    conx = sqlite3.connect("Payroll.db")
    return conx

''' connect to db and read data with a limit
get data from database
return a pandas '''

def get_agencydata(): 
    con = get_conx()
    agency_data = pd.read_sql_query("SELECT * FROM AGENCY;",con ,)
    agency_data = agency_data.head(165)
    agencydf = pd.DataFrame(agency_data)
    con.close()
    return agencydf

#get data from empoyee table
def get_employeedata(): 
    con = get_conx()
    employee_data = pd.read_sql_query("SELECT * FROM EMPLOYEE;",con, index_col='employee_id')
    employee_data = employee_data.head(100)
    employeedf = pd.DataFrame(employee_data)
    con.close()
    return employeedf

#get data from payroll table
def get_payrolldata(): 
    con = get_conx()
    payroll_data = pd.read_sql_query("SELECT * FROM PAYROLL;",con)
    con.close()
    payrolldf = pd.DataFrame(payroll_data)
    payrolldf = payroll_data.head(100)
    return payrolldf

def get_colors():
    txt_file = open("colors.txt", "r")
    file_content = txt_file.read()
    content_list = file_content.split("\n")
    txt_file.close()
    return content_list
    
    
def get_department_totals():
    con = get_conx()
    department_data = pd.read_sql_query("SELECT * FROM department_totals;",con)
    department_data = department_data.head(165)
    departmentdf = pd.DataFrame(department_data)
    con.close()
    return departmentdf

def get_highest_earners():
    con = get_conx()
    highestearners_data = pd.read_sql_query("SELECT * FROM highest_earners;",con)
    highestearnersdf = pd.DataFrame(highestearners_data)
    con.close()
    return highestearnersdf