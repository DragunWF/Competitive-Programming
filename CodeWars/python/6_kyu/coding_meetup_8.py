# https://www.codewars.com/kata/coding-meetup-number-8-higher-order-functions-series-will-all-continents-be-represented

def all_continents(developers: list[dict]) -> bool:
    continents_present = {
        "Africa": False, "Americas": False, "Asia": False,
        "Europe": False, "Oceania": False
    }
    for developer in developers:
        continents_present[developer["continent"]] = True
    return all(continents_present.values())


def test() -> None:
    print(all_continents(
        [
            {'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria',
                'continent': 'Africa', 'age': 25, 'language': 'JavaScript'},
            {'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile',
                'continent': 'Americas', 'age': 37, 'language': 'C'},
            {'firstName': 'Jing', 'lastName': 'X.', 'country': 'China',
                'continent': 'Asia', 'age': 39, 'language': 'Ruby'},
            {'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra',
                'continent': 'Europe', 'age': 55, 'language': 'Ruby'},
            {'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia',
                'continent': 'Oceania', 'age': 65, 'language': 'PHP'}
        ]
    ))


if __name__ == "__main__":
    test()
