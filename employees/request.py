import sqlite3
import json
from models import Employee, Location

EMPLOYEES = [
     {
      "id": 1,
      "name": "Jeremy Baker",
      "locationId": 1
    },
    {
      "id": 2,
      "name": "Linda McDoogle",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Jackie Tortellini",
      "locationId": 1
    }
]

def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id,
            b.name location_name,
            b.address location_address
        FROM employee a
        JOIN Location b
            ON b.id = a.location_id;
        """)

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            location = Location(row['id'], row['location_name'], row['location_address'])
            employee.location = location.__dict__
            employees.append(employee.__dict__)

    return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE a.id = ?
        """, ( id, ))
    
    data = db_cursor.fetchone()

    employee = Employee(data['id'], data['name'], data['address'], data['location_id'])
    return json.dumps(employee.__dict__)

def create_employee(employee):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
    
        db_cursor.execute("""
        INSERT INTO Employee
            ( name, address, location_id)
        VALUES
            (?, ?, ?)
        """, (employee['name'], employee['address'], employee['location_id']))
        id = db_cursor.lastrowid
        employee['id'] = id
    return json.dumps(employee)


def delete_employee(id):
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index
    
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break

def get_employees_by_location(location_id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.location_id
        FROM Employee c
        WHERE c.location_id = ?
        """, (location_id, ))
        employees = []
        dataset = db_cursor.fetchall()
        for data in dataset:
            employee = Employee(data['id'], data['name'], data['address'], data['location_id'])
            employees.append(employee.__dict__)
    return json.dumps(employees)