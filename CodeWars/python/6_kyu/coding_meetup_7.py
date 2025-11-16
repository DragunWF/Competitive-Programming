# https://www.codewars.com/kata/coding-meetup-number-7-higher-order-functions-series-find-the-most-senior-developer

def find_senior(developers: list[dict]) -> list[dict]:
    oldest_age = max(developer["age"] for developer in developers)
    return list(filter(lambda developer: developer["age"] == oldest_age, developers))


def test() -> None:
    print(find_senior([
        {'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco',
            'continent': 'Europe', 'age': 49, 'language': 'PHP'},
        {'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia',
            'continent': 'Asia', 'age': 38, 'language': 'Python'},
        {'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania',
            'continent': 'Europe', 'age': 19, 'language': 'Python'},
        {'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan',
            'continent': 'Asia', 'age': 49, 'language': 'PHP'},
    ]))


if __name__ == "__main__":
    test()
