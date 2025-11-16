# https://www.codewars.com/kata/coding-meetup-number-9-higher-order-functions-series-is-the-meetup-age-diverse

def is_age_diverse(developers: list[dict]) -> bool:
    age_groups_met = {
        "teens": False, "twenties": False, "thirties": False, "forties": False,
        "fifties": False, "sixties": False, "seventies": False, "eighties": False,
        "nineties": False, "centenarian": False
    }
    for developer in developers:
        age = developer["age"]
        if age < 20:
            age_groups_met["teens"] = True
        elif age < 30:
            age_groups_met["twenties"] = True
        elif age < 40:
            age_groups_met["thirties"] = True
        elif age < 50:
            age_groups_met["forties"] = True
        elif age < 60:
            age_groups_met["fifties"] = True
        elif age < 70:
            age_groups_met["sixties"] = True
        elif age < 80:
            age_groups_met["seventies"] = True
        elif age < 90:
            age_groups_met["eighties"] = True
        elif age < 100:
            age_groups_met["nineties"] = True
        else:
            age_groups_met["centenarian"] = True
    return all(age_groups_met.values())


def test() -> None:
    print(is_age_diverse([
        {'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil',
            'continent': 'Americas', 'age': 19, 'language': 'Python'},
        {'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus',
            'continent': 'Europe', 'age': 29, 'language': 'JavaScript'},
        {'firstName': 'Jing', 'lastName': 'X.', 'country': 'China',
            'continent': 'Asia', 'age': 39, 'language': 'Ruby'},
        {'firstName': 'Noa', 'lastName': 'A.', 'country': 'Israel',
            'continent': 'Asia', 'age': 40, 'language': 'Ruby'},
        {'firstName': 'Andrei', 'lastName': 'E.', 'country': 'Romania',
            'continent': 'Europe', 'age': 59, 'language': 'C'},
        {'firstName': 'Maria', 'lastName': 'S.', 'country': 'Peru',
            'continent': 'Americas', 'age': 60, 'language': 'C'},
        {'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia',
            'continent': 'Europe', 'age': 75, 'language': 'Python'},
        {'firstName': 'Chloe', 'lastName': 'K.', 'country': 'Guernsey',
            'continent': 'Europe', 'age': 88, 'language': 'Ruby'},
        {'firstName': 'Viktoria', 'lastName': 'W.', 'country': 'Bulgaria',
            'continent': 'Europe', 'age': 98, 'language': 'PHP'},
        {'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland',
            'continent': 'Europe', 'age': 128, 'language': 'JavaScript'}
    ]))  # True


if __name__ == "__main__":
    test()
