# https://www.codewars.com/kata/58381907f8ac48ae070000de/train/python

def is_language_diverse(developers: list[dict]) -> bool:
    language_counter = {"Python": 0, "Ruby": 0, "JavaScript": 0}
    for developer in developers:
        language = developer["language"]
        if language in language_counter:
            language_counter[language] += 1
    for language, count in language_counter.items():
        for compared_language, compared_count in language_counter.items():
            if language == compared_language:
                continue
            if count > compared_count * 2:
                return False
    return True


def test() -> None:
    print(is_language_diverse([
        {'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba',
            'continent': 'Americas', 'age': 42, 'language': 'Python'},
        {'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus',
            'continent': 'Europe', 'age': 22, 'language': 'Ruby'},
        {'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan',
            'continent': 'Asia', 'age': 43, 'language': 'Ruby'},
        {'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary',
            'continent': 'Europe', 'age': 95, 'language': 'JavaScript'},
        {'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica',
            'continent': 'Americas', 'age': 18, 'language': 'JavaScript'},
        {'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal',
            'continent': 'Europe', 'age': 25, 'language': 'JavaScript'}
    ]))  # False
    print(is_language_diverse([
          {'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba',
              'continent': 'Americas', 'age': 42, 'language': 'Python'},
          {'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus',
              'continent': 'Europe', 'age': 22, 'language': 'Ruby'},
          {'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica',
              'continent': 'Americas', 'age': 18, 'language': 'JavaScript'},
          {'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal',
              'continent': 'Europe', 'age': 25, 'language': 'JavaScript'}
          ]))  # True


if __name__ == "__main__":
    test()
