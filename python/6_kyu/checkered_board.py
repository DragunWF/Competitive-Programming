# https://www.codewars.com/kata/5650f1a6075b3284120000c0/train/python

def checkered_board(n: int) -> str:
    board: list[str] = []
    alternate = n % 2 != 0
    for i in range(n):
        row = []
        for j in range(n):
            is_even = (j + 1) % 2 == 0
            if alternate:
                row.append("\u25A1" if is_even else "\u25A0")
            else:
                row.append("\u25A0" if is_even else "\u25A1")
        board.append(" ".join(row))
        alternate = not alternate
    return "\n".join(board)
