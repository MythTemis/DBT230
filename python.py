import os

#-------Employee Class----------------
class Employee:
    def __init__(self, id, firstName, lastName, hireYear):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.hireYear = hireYear
    
    def __str__(employee):
        return ("\nEmployee ID: " + employee.id +
            "\nFirst Name: " + employee.firstName +
            "\nLast Name: " + employee.lastName + 
            "\nHire Year: " + employee.hireYear
            )

#--------------------------------------------------------
SIMPLE_PATH = r'C:\Users\atemple\source\repos\DBT230\DBT230\Assignment 1 - data\people\simple/'

#SIMPLE_PATH = r'C:\Users\zhenx\Desktop\Assignment 1 - data (3)\people\simple/'

def print_people_details(path):
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            f = open(os.path.join(path, file), 'r')
            for x in f: 
                print(x)
            f.close()

def print_employee(path):
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            f = open(os.path.join(path, file), 'r')
            for x in f: 
                string = x
                information = string.split()
                id = information[0]
                fName = information[1]
                lName = information[2]
                hireYear = information[3]
                employee = Employee(id,fName,lName,hireYear)
                print(employee)
            f.close()

def add_employee(id, first, last, year):
    nfile = os.write("%s.csv" % id, "w")
    #put the file in the place
    #add the rest of the values
    #write

def update_employee(id, first_name, last_name, hire_date):
    file_name = str(id) + ".txt"
    file_path = SIMPLE_PATH + file_name
    if os.path.isfile(file_path):
        file_reference = open(file_path, "w")
        string_to_write = ", ".join([str(id), first_name, last_name, str(hire_date),])
        file_reference.write(string_to_write)
        file_reference.close()


print_people_details(SIMPLE_PATH)
print_employee(SIMPLE_PATH)
update_employee(44545, "firstName", "lastName", )

