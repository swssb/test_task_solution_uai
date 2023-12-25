import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        salary FLOAT NOT NULL
    )
""")
conn.commit()


class Employee:
    def __init__(self, id: int, name: str, salary: float):
        self.id = id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'Employee ID: {self.id}, Name: {self.name}, Salary: {self.salary}'


def create_employee(name: str, salary: float):
    cursor.execute("INSERT INTO employees (name, salary) VALUES (?, ?)", (name, salary))
    conn.commit()
    return cursor.lastrowid


def get_employee(employee_id: int):
    cursor.execute("SELECT * FROM employees WHERE id=?", (employee_id,))
    row = cursor.fetchone()
    if row:
        return Employee(id=row[0], name=row[1], salary=row[2])
    else:
        return None


def get_all_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    employees = [Employee(id=row[0], name=row[1], salary=row[2]) for row in rows]
    return employees


def update_employee(employee_id: int, name: str, salary: float):
    cursor.execute("UPDATE employees SET name=?, salary=? WHERE id=?", (name, salary, employee_id))
    conn.commit()


def delete_employee(employee_id: int):
    cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
    conn.commit()


create_employee('Viktor', 100)
create_employee('Valeriy', 350)
create_employee('Nikita', 890.50)

all_employees = get_all_employees()
for employee in all_employees:
    print(employee)
print(get_employee(1))
update_employee(1, name='Viktor', salary=500)
print(get_employee(1))
delete_employee(2)
