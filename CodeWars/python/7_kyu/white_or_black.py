# https://www.codewars.com/kata/563319974612f4fa3f0000e0/train/python

def square_color(file: str, rank: int) -> str:
    letter_notation = "abcdefgh"
    letter_index = letter_notation.index(file)
    is_even_letter = letter_index % 2 == 0
    if is_even_letter:
        return "white" if rank % 2 == 0 else "black"
    return "black" if rank % 2 == 0 else "white"
