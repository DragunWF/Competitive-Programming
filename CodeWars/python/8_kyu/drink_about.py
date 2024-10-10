# https://www.codewars.com/kata/56170e844da7c6f647000063

def people_with_age_drink(age):
    category, ages = {14: "drink toddy",
                      18: "drink coke", 21: "drink beer"}, (14, 18, 21)
    for x in ages:
        if age < x:
            return category[x]
    return "drink whisky"
