# https://www.codewars.com/kata/57ebdf1c2d45a0ecd7002cd5/train/python

def inside_out(s: str) -> str:
    words = s.split(" ")
    output = []
    for word in words:
        mid = len(word) // 2
        if len(word) % 2 == 0:
            output.append(f"{word[:mid][::-1]}{word[mid:][::-1]}")
        else:
            output.append(
                f"{word[:mid][::-1]}{word[mid]}{word[mid + 1:][::-1]}"
            )
    return " ".join(output)


def test() -> None:
    # Expected: atix atxsi
    print(inside_out("taxi taxis"))

    # Expected: man i ende a atix up to budu
    print(inside_out("man i need a taxi up to ubud"))


if __name__ == "__main__":
    test()

# 'cbafed gfedcbanmlkjih dcbahgfe edcbajihgf hgfedcbaponmlkji lkjihgfedcbamyxwvutsrqpon hgfedcbaponmlkji cbafed dcbaeihgf gfedcbahonmlkji kjihgfedcbavutsrqponml dcbaeihgf baced badc lkjihgfedcbaxwvutsrqponm' should equal
# 'cbafed gfedcbanmlkjih dcbahgfe edcbajihgf hgfedcbaponmlkji lkjihgfedcbamyxwvutsrqpon hgfedcbaponmlkji cbafed dcbaeihgf gfedcbahonmlkji kjihgfedcbavutsrqponml dcbaeihgf baced  badc lkjihgfedcbaxwvutsrqponm'

# 'gfedcbanmlkjih hgfedcbaponmlkji lkjihgfedcbaxwvutsrqponm ihgfedcbajsrqponmlk dcbaeihgf cbafed ab edcbajihgf lkjihgfedcbamyxwvutsrqpon gfedcbanmlkjih jihgfedcbakutsrqponml hgfedcbaiqponmlkj jihgfedcbatsrqponmlk lkjihgfedcbaxwvutsrqponm a' should equal
# 'gfedcbanmlkjih hgfedcbaponmlkji lkjihgfedcbaxwvutsrqponm ihgfedcbajsrqponmlk dcbaeihgf cbafed ab edcbajihgf lkjihgfedcbamyxwvutsrqpon gfedcbanmlkjih jihgfedcbakutsrqponml hgfedcbaiqponmlkj  jihgfedcbatsrqponmlk lkjihgfedcbaxwvutsrqponm a '
