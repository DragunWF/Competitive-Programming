# https://www.codewars.com/kata/62a611067274990047f431a8/train/javascript

def alternate(n: int, first_value, second_value) -> list:
    output = []
    for i in range(n):
        output.append(first_value if i % 2 == 0 else second_value)
    return output


def test() -> None:
    # -->  [true, false, true, false, true]
    print(alternate(5, True, False))
    # -->  ["blue", "red", "blue", "red", "blue", "red", "blue", "red", "blue", "red"]
    print(alternate(10, "blue", "red"))
    print(alternate(0, "one", "two"))    # -->  []


if __name__ == "__main__":
    test()
