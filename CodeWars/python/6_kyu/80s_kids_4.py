# https://www.codewars.com/kata/56648a2e2c464b8c030000bf/train/python

def mark_spot(n: int) -> str:
    if not type(n) is int or n % 2 == 0 or n < 0:
        return "?"
    if n == 1:
        return "X\n"
    edge_whitespace_count = 0
    middle_whitespace_count = n * 2 - 3
    output = []
    for i in range(n):
        edges = " " * edge_whitespace_count
        middle = " " * middle_whitespace_count
        output.append(f"{edges}X{middle}X" if i != n // 2 else f"{edges}X")
        if i < n // 2:
            edge_whitespace_count += 2
            middle_whitespace_count = max(middle_whitespace_count - 4, -1)
        else:
            edge_whitespace_count -= 2
            middle_whitespace_count += 4
    return "\n".join(output) + "\n"


def test() -> None:
    print(mark_spot(5))


if __name__ == "__main__":
    test()
