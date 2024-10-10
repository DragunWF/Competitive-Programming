# https://www.codewars.com/kata/568dc014440f03b13900001d/train/python

def get_drink_by_profession(param: str) -> str:
    try:
        return {
            "jabroni": "Patron Tequila", "school counselor": "Anything with Alcohol",
            "programmer": "Hipster Craft Beer", "bike gang member": "Moonshine",
            "politician": "Your tax dollars", "rapper": "Cristal"
        }[param.lower()]
    except KeyError:
        return "Beer"
