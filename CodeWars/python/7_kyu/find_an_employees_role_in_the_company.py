# https://www.codewars.com/kata/55c9fb1b407024afe6000055/train/python

# Preloaded in the Kata
employees: list[dict] = [
    {'first_name': 'Ollie', 'last_name': 'Hepburn', 'role': 'Boss'},
    {'first_name': 'Morty', 'last_name': 'Smith', 'role': 'Truck Driver'},
    {'first_name': 'Peter', 'last_name': 'Ross', 'role': 'Warehouse Manager'},
    {'first_name': 'Cal', 'last_name': 'Neil', 'role': 'Sales Assistant'},
    {'first_name': 'Jesse', 'last_name': 'Saunders', 'role': 'Admin'},
    {'first_name': 'Anna', 'last_name': 'Jones', 'role': 'Sales Assistant'},
    {'first_name': 'Carmel', 'last_name': 'Hamm', 'role': 'Admin'},
    {'first_name': 'Tori', 'last_name': 'Sparks', 'role': 'Sales Manager'},
    {'first_name': 'Peter', 'last_name': 'Jones', 'role': 'Warehouse Picker'},
    {'first_name': 'Mort', 'last_name': 'Smith', 'role': 'Warehouse Picker'},
    {'first_name': 'Anna', 'last_name': 'Bell', 'role': 'Admin'},
    {'first_name': 'Jewel', 'last_name': 'Bell', 'role': 'Receptionist'},
    {'first_name': 'Colin', 'last_name': 'Brown', 'role': 'Trainee'}
]


def find_employees_role(name: str) -> str:
    name_parts = name.split(" ")
    first_name = name_parts[0]
    last_name = None
    if len(name_parts) > 1:
        last_name = name_parts[1]
    for employee in employees:
        if first_name == employee["first_name"] and last_name == employee["last_name"]:
            return employee["role"]
    return "Does not work here!"
