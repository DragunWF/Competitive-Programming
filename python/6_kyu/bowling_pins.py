# https://www.codewars.com/kata/585cf93f6ad5e0d9bf000010/train/python

def bowling_pins(arr: list[int]) -> str:
    rows = []

    def new_row(start: int, end: int) -> None:
        current_row = []
        for i in range(start, end + 1):
            current_row.append("I" if not i in arr else " ")
        return " ".join(current_row)

    rows.append(new_row(7, 10))
    rows.append(f" {new_row(4, 6)} ")
    rows.append(f"  {new_row(2, 3)}  ")
    rows.append("       " if 1 in arr else "   I   ")

    return "\n".join(rows)


# Test code
print(bowling_pins([2, 3]))
