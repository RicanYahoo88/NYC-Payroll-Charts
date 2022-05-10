from optparse import Values
from flask import Flask, render_template, send_file, make_response, url_for, Response
from flask_bootstrap import Bootstrap
from table_data import *
import pandas as pd

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/tables')
def get_tables():
    return render_template('tables.html')

@app.route('/agencytable', methods=("POST", "GET"))
def get_agencytable():
    agency_data = get_agencydata()
    return render_template('agency.html', PageTitle = "Agency Table", table=[agency_data.to_html(classes='data', index = False)], titles= agency_data.columns.values)

@app.route('/employeetable', methods=("POST", "GET"))
def get_employeetable():
    employee_data = get_employeedata()
    return render_template('employee.html', PageTitle = "Employee Table", table=[employee_data.to_html(classes='data', index = False)], titles= employee_data.columns.values)

@app.route('/payrolltable', methods=("POST", "GET"))
def get_payrolltable():
    payroll_data = get_payrolldata()
    return render_template('payrolltable.html', PageTitle = "Payroll Table", table=[payroll_data.to_html(classes='data', index = False)], titles= payroll_data.columns.values)

@app.route('/graphs')
def get_graphs():
    return render_template('graphs.html')

@app.route('/payrollcharts')
def get_payrollcharts():
    # create pie chart
    departmentdf = get_department_totals()
    pie_labels = departmentdf['agency_name'].values
    pie_values = departmentdf['department_total'].values
    colors = get_colors()
    
    #create bar chart
    highest_earnersdf = get_highest_earners()
    bar_labels = highest_earnersdf['first_name'].values + " " + highest_earnersdf['last_name'].values
    bar_values = highest_earnersdf['gross_sum'].values
    return render_template('payrollcharts.html', title='Payroll Charts', pie_title='Payroll by Agency(top 25)', pie_max=17000, pie_set=zip(pie_values, pie_labels, colors), bar_title='Highest Earners(top 12)', bar_max=700000, bar_labels = bar_labels, bar_values = bar_values )





