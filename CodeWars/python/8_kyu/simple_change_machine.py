# https://www.codewars.com/kata/57238766214e4b04b8000011

def change_me(money: str) -> str:
    changes = {
        "£5": "20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p 20p",
        "£2": "20p 20p 20p 20p 20p 20p 20p 20p 20p 20p",
        "£1": "20p 20p 20p 20p 20p",
        "50p": "20p 20p 10p",
        "20p": "10p 10p"
    }
    return changes[money] if money in changes else money


def change_me_case(money: str) -> str:
    match money:
        case "£5":
            return "£2 £2 £1"
        case "£2":
            return "£1 £1"
        case "£1":
            return "50p 50p"
        case "50p":
            return "20p 20p 10p"
        case "20p":
            return "10p 10p"
        case _:
            return money


def change_me_incomplete(money: str) -> str:
    if money[-1] != "p" or money[-1] != "£":
        return money

    try:
        total_money = int(money[:-1])
        if total_money[-1] == "£":
            total_money *= 100

        coins = []
        while total_money > 0:
            if 200 <= total_money < 500:
                pass
            elif 100 <= total_money < 200:
                pass
            elif total_money < 100:
                pass
            elif total_money < 50:
                pass
            elif total_money < 20:
                pass
        return " ".join(coins)
    except ValueError:
        return money


def test() -> None:
    # Expected: 20p 20p 20p
    print(change_me("50p"))


if __name__ == "__main__":
    test()
