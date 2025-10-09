# https://www.codewars.com/kata/585eaef9851516fcae00004d/train/python

def what_list_am_i_on(actions: list[str]) -> str:
    naughty_count = 0
    nice_count = 0
    for action in actions:
        if action.startswith("b") or action.startswith("f") or action.startswith("k"):
            naughty_count += 1
        elif action.startswith("g") or action.startswith("s") or action.startswith("n"):
            nice_count += 1
    return "nice" if nice_count > naughty_count else "naughty"


def test() -> None:
    # Expected: 'naughty'
    print(what_list_am_i_on(['broke someone\'s window',
          'fought over a toaster', 'killed a bug']))


if __name__ == "__main__":
    test()
