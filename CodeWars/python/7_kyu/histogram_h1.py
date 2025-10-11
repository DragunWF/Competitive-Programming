# https://www.codewars.com/kata/57d532d2164a67cded0001c7/train/python

def histogram(results: list[int]) -> str:
    output = []
    for i in range(len(results), 0, -1):
        count = results[i - 1]
        if count == 0:
            output.append(f"{i}|")
            continue
        output.append(f"{i}|{'#' * count} {count}")
    return "\n".join(output) + "\n"


def test() -> None:
    print(histogram([7, 3, 10, 1, 0, 5]))


if __name__ == "__main__":
    test()
