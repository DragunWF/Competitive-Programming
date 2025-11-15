# https://www.codewars.com/kata/5650ab06d11d675371000003

def split_in_parts(s: str, part_length: int) -> str:
    parts = []
    current_part = ""
    for i, char in enumerate(s):
        current_part += char
        if (i + 1) % part_length == 0:
            parts.append(current_part)
            current_part = ""
    if current_part:
        parts.append(current_part)
    return " ".join(parts)


def test() -> None:
    # Expected: 'sup erc ali fra gil ist ice xpi ali doc iou s'
    print(split_in_parts('supercalifragilisticexpialidocious', 3))


if __name__ == "__main__":
    test()
