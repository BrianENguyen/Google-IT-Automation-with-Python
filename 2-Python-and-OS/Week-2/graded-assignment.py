#!/usr/bin/env python3

'''
The goal of the script is to read the CSV file and generate
a report with the toal number of people in each department
'''
import csv
def read_employees(csv_file_location):
        csv.register_dialect('empDialect', skipinitialspace=True, 
strict=True)
        employee_file = csv.DictReader(open(csv_file_location), dialect 
= 'empDialect')
        employee_list = []
        for data in employee_file:
                employee_list.append(data)
        return employee_list
employee_list = 
read_employees('/home/student-03-1407e4b45407/data/employees.csv')

def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])
        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = 
department_list.count(department_name)
        return department_data

dictionary = process_data(employee_list)

def write_report(dictionary, report_file):
        with open(report_file, 'w+') as file:
                for k in sorted(dictionary):
                        file.write(str(k)+':'+str(dictionary[k])+'\n')
                file.close()

write_report(dictionary, 
'/home/student-03-1407e4b45407/test_report.txt')

