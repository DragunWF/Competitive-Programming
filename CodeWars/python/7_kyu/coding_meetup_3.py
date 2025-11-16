# https://www.codewars.com/kata/coding-meetup-number-3-higher-order-functions-series-is-ruby-coming

def is_ruby_coming(users: list[dict]) -> bool:
    for user in users:
        if user["language"] == "Ruby":
            return True
    return False


def test() -> None:
    print(is_ruby_coming([
        {'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina',
            'continent': 'Americas', 'age': 35, 'language': 'Java'},
        {'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia',
            'continent': 'Europe', 'age': 35, 'language': 'Python'},
        {'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States',
            'continent': 'Americas', 'age': 32, 'language': 'Ruby'}
    ]))


if __name__ == "__main__":
    test()
