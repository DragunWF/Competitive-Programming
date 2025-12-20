# https://www.codewars.com/kata/5592e5d3ede9542ff0000057/train/python

def pattern(n: int, x: int = 1, *args) -> str:
    if n < 1:
        return ""
    if x < 1:
        x = 1

    output = []
    middle_whitespace_count = n * 2 - 3
    edge_whitespace_count = 0

    for i in range(1, n * 2):
        num = (n - abs(n - i)) % 10

        middle = " " * max(0, middle_whitespace_count)
        edges = " " * edge_whitespace_count

        between_gap_size = (edge_whitespace_count * 2) - 1

        if middle_whitespace_count >= 0:
            unit = f"{num}{middle}{num}"

            if between_gap_size < 0:
                row_content = f"{num}" + (f"{middle}{num}" * x)
            else:
                gap = " " * between_gap_size
                row_content = gap.join([unit] * x)
        else:
            center_gap = " " * (n * 2 - 3)
            row_content = center_gap.join([str(num)] * x)

        output.append(f"{edges}{row_content}{edges}")

        if i < n:
            middle_whitespace_count -= 2
            edge_whitespace_count += 1
        else:
            middle_whitespace_count += 2
            edge_whitespace_count -= 1

    return "\n".join(output)


def test() -> None:
    print(pattern(4, 3))
    print(pattern(3, 7))


if __name__ == "__main__":
    test()
