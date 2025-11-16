# https://www.codewars.com/kata/58287977ef8d4451f90001a0/train/python

def is_same_language(developers: list[dict]) -> bool:
    return len(set(developer["language"] for developer in developers)) == 1


def test() -> None:
    print(is_same_language([
        {'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland',
            'continent': 'Europe', 'age': 19, 'language': 'C'},
        {'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein',
            'continent': 'Europe', 'age': 52, 'language': 'JavaScript'},
        {'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay',
            'continent': 'Americas', 'age': 29, 'language': 'Ruby'},
        {'firstName': 'George', 'lastName': 'B.', 'country': 'England',
            'continent': 'Europe', 'age': 81, 'language': 'C'},
    ]))


if __name__ == "__main__":
    test()
