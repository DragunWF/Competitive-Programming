# https://www.codewars.com/kata/5827bc50f524dd029d0005f2

def get_first_python(users: list[dict]) -> str:
    for user in users:
        if user["language"] == "Python":
            return f"{user['first_name']}, {user['country']}"
    return "There will be no Python developers"


def test() -> None:
    print(get_first_python([
        {"first_name": "Mark", "last_name": "G.", "country": "Scotland",
            "continent": "Europe", "age": 22, "language": "JavaScript"},
        {"first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico",
            "continent": "Americas", "age": 30, "language": "Python"},
        {"first_name": "Emma", "last_name": "B.", "country": "Norway",
            "continent": "Europe", "age": 19, "language": "Clojure"}
    ]))


if __name__ == "__main__":
    test()
