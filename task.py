import psycopg2

# connect to db
con = psycopg2.connect(
    host="localhost",
    database="pythonoop",
    user="postgres",
    password="172733"
)

print('Database opened successfully')

# cursor
cur = con.cursor()


class employee:

    employee_list = []

    def __init__(self, id, fname, lname, age, department, salary):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age
        self.department = department
        self.salary = salary

        employee.employee_list.append({
            'ID': self.id,
            'First Name': self.fname,
            'last Name': self.lname,
            'Age': self.age,
            'Department': self.department,
            'Salary': self.salary
        })

        cur.execute(
            "insert into employee (id,fname,lname,age,department,salary) values (%s,%s,%s,%s,%s,%s)", (self.id, self.fname, self.lname, self.age, self.department, self.salary))

    @classmethod
    def transfer(cls, department, id):
        cls.department = department
        cls.id = id

        cur.execute(
            "update employee set department = %s where id = %s", (cls.department, cls.id))

    @staticmethod
    def fire(self):
        cur.execute("delete from employee where id = %s", self.id)

    def show(self):
        print(employee.employee_list)

    def list_employee():
        cur.execute("select * from employee;")
        rows = cur.fetchall()
        for r in rows:
            print(
                f"id: {r[0]} fname: {r[1]} lname: {r[2]} age: {r[3]} department: {r[4]} salary: {r[5]}")


class Manger(employee):

    mangers_list = []

    def __init__(self, Managed_department, id, fname, lname, age, department, salary):
        super().__init__(id, fname, lname, age, department, salary)
        self.Managed_department = Managed_department

        Manger.mangers_list.append({
            'Managed_department': self.Managed_department,
            'ID': self.id,
            'First Name': self.fname,
            'last Name': self.lname,
            'Age': self.age,
            'Department': self.department
        })

        cur.execute(
            "insert into mangers (id,fname,lname,age,department,Managed_department,salary) values (%s,%s,%s,%s,%s,%s,%s)", (self.id, self.fname, self.lname, self.age, self.department, self.Managed_department, self.salary))

    def show(self):
        print(Manger.mangers_list)


print(' \nFor add new employee enter add \nFor transfer new employee enter transfer \nFor fire new employee enter fire \nFor show new employe enter show \nfor list_employee enter list')
input_1 = input('')
if input_1 == "add":
    print("for employee enter e for manger enter m")
    a = input("")
    if a == "e":
        ID = int(input('Enter employee ID: '))
        First_name = input('Enter employee first name: ')
        Last_name = input('Enter employee second name: ')
        Age = int(input('Enter employee age: '))
        Department = input('Enter employee department: ')
        Salary = int(input('Enter employee Salary: '))

        emp_1 = employee(ID, First_name, Last_name, Age, Department, Salary)

    elif a == "m":
        Managed_department = input('Enter Manged department: ')
        ID = int(input('Enter Manger ID: '))
        First_name = input('Enter Manger first name: ')
        Last_name = input('Enter Manger second name: ')
        Age = int(input('Enter Manger age: '))
        Department = input('Enter manger department: ')
        Salary = int(input('Enter Manger Salary: '))

        mgr_1 = Manger(Managed_department, ID, First_name, Last_name,
                       Age, Department, Salary)
    else:
        exit
if input_1 == "transfer":
    print("for employee enter e for manger enter m")
    a = input("")
    if a == "e":
        employee.transfer('DevOS', 8)

    elif a == "m":
        Manger.transfer('DevOS', 8)

    else:
        exit
if input_1 == "fire":
    print("for employee enter e for manger enter m")
    a = input("")
    if a == "e":
        employee.fire(9)

    elif a == "m":
        Manger.fire(9)

    else:
        exit
if input_1 == "show":
    print("for employee enter e for manger enter m")
    a = input("")
    if a == "e":
        emp_1.show()

    elif a == "m":
        mgr_1.show()

    else:
        exit
if input_1 == "list":
    print("for employee enter e for manger enter m")
    a = input("")
    if a == "e":
        employee.list_employee()

    elif a == "m":
        Manger.list_employee()

    else:
        exit
else:
    exit


# commit the transaction
con.commit()

# close cursor
cur.close()

# close the connection
con.close()
