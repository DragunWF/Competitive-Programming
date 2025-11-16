# https://www.codewars.com/kata/5828713ed04efde70e000346/train/python

def count_languages(users: list[dict]) -> dict:
    output = {}
    for user in users:
        language = user["language"]
        if not language in output:
            output[language] = 1
        else:
            output[language] += 1
    return output


def test() -> None:
    print(count_languages([
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
