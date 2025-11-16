# https://www.codewars.com/kata/582ba36cc1901399a70005fc/train/python

def get_average(data: list) -> int:
    return round(sum(person["age"] for person in data) / len(data))


def test() -> None:
    # Expected: 50
    print(get_average([
        {'firstName': 'Maria', 'lastName': 'Y.', 'country': 'Cyprus',
            'continent': 'Europe', 'age': 30, 'language': 'Java'},
        {'firstName': 'Victoria', 'lastName': 'T.', 'country': 'Puerto Rico',
            'continent': 'Americas', 'age': 70, 'language': 'Python'},
    ]))


if __name__ == "__main__":
    test()
