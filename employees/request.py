import sqlite3
import json
from models import Employee, animal

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
            a.location_id
        FROM employee a
        """)

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['location_id'])
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
            a.location_id
        FROM employee a
        WHERE a.id = ?
        """, ( id, ))
    
    data = db_cursor.fetchone()

    employee = Employee(data['id'], data['name'], data['location_id'])
    return json.dumps(employee.__dict__)

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee

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