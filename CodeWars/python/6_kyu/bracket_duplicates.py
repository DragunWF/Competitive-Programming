# https://www.codewars.com/kata/5411c4205f3a7fd3f90009ea/train/python

def string_parse(s: str) -> str:
    if not type(s) is str:
        return "Please enter a valid string"
    if not s:
        return ""
    parsed_chunks = []
    prev_char = s[0]
    current_chunk = [prev_char]
    for i, char in enumerate(s[1:]):
        if char == prev_char:
            if len(current_chunk) == 2:
                current_chunk.append("[")
            current_chunk.append(char)
        elif char != prev_char or i == len(s) - 1:
            if len(current_chunk) > 2:
                current_chunk.append("]")
            parsed_chunks.append("".join(current_chunk))
            current_chunk.clear()
            current_chunk.append(char)
        prev_char = char
    if len(current_chunk) > 0:
        parsed_chunks.append("".join(current_chunk))
        if len(current_chunk) > 2:
            parsed_chunks.append("]")
    return "".join(parsed_chunks)


def test() -> None:
    # Expected: "aa[aa]bbcdeff[fffff]g"
    print(string_parse("aaaabbcdefffffffg"))

    # Expected: "dd[d]cc[cc]"
    print(string_parse("dddcccc"))


if __name__ == "__main__":
    test()
