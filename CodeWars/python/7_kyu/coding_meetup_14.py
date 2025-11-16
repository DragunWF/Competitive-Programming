# https://www.codewars.com/kata/583952fbc23341c7180002fd/python

def order_food(users: list[dict]) -> dict:
    food_options = {}
    for user in users:
        meal = user["meal"]
        if not meal in food_options:
            food_options[meal] = 1
        else:
            food_options[meal] += 1
    return food_options


def test() -> None:
    print(order_food([
        {'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland',
            'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian'},
        {'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein',
            'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard'},
        {'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay',
            'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan'},
        {'firstName': 'George', 'lastName': 'B.', 'country': 'England',
            'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian'},
    ]))


if __name__ == "__main__":
    test()
