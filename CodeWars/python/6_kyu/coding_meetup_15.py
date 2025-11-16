# https://www.codewars.com/kata/coding-meetup-number-15-higher-order-functions-series-find-the-odd-names

def find_odd_names(persons: list[dict]) -> list[dict]:
    odd_people = []
    for person in persons:
        ascii_sum = 0
        for char in person["firstName"]:
            ascii_sum += ord(char)
        if ascii_sum % 2 != 0:
            odd_people.append(person)
    return odd_people


def test() -> None:
    print(find_odd_names([
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
