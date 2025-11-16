# https://www.codewars.com/kata/coding-meetup-number-12-higher-order-functions-series-find-github-admins

def find_admin(developers: list[dict], lang: str):
    admins = []
    for developer in developers:
        if developer["language"] == lang and developer["githubAdmin"] == "yes":
            admins.append(developer)
    return admins


def test() -> None:
    print(find_admin([
        {'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil',
            'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes'},
        {'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus',
            'continent': 'Europe', 'age': 49, 'language': 'Ruby', 'githubAdmin': 'no'},
        {'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia',
            'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes'},
        {'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland',
            'continent': 'Europe', 'age': 128, 'language': 'JavaScript', 'githubAdmin': 'no'}
    ], "JavaScript"))


if __name__ == "__main__":
    test()
