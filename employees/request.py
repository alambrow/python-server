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
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee