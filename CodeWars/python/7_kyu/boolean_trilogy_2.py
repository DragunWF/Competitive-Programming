# https://www.codewars.com/kata/5f8070c834659f00325b5313/train/python

def calculate(expr: str, values: dict[str, int]) -> int:
    for key in values:
        expr = expr.replace(key, str(values[key]))
    expr = expr.replace("1", "True").replace("0", "False")
    expr = expr.replace("&", "and").replace("|", "or")
    return int(eval(expr))


def test() -> None:
    # print(eval("True and True"))
    # print(calculate("A & B & C", {"A": 0, "B": 1, "C": 0}))  # 0
    # print(calculate("B & A | C", {"A": 1, "B": 0, "C": 1}))  # returns 1
    print(calculate("B | D | A & B | C | B & C & F | D | C & F & C | E",
          {'A': 1, 'B': 0, 'C': 1, 'D': 1, 'E': 0, 'F': 1}))


if __name__ == "__main__":
    test()
