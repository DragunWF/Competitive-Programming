# https://www.codewars.com/kata/628e3ee2e1daf90030239e8a/train/python

def interlockable(a: int, b: int) -> bool:
    a_bin = bin(a)[2:]
    b_bin = bin(b)[2:]
    max_len = max(len(a_bin), len(b_bin))
    if len(a_bin) < max_len:
        a_bin = pad_binary(a_bin, max_len)
    if len(b_bin) < max_len:
        b_bin = pad_binary(b_bin, max_len)
    for i in range(max_len):
        if a_bin[i] == "1" and b_bin[i] == "1":
            return False
    return True


def pad_binary(n: str, required_len: int) -> str:
    missing_count = required_len - len(n)
    return "0" * missing_count + n


def test() -> None:
    print(pad_binary("1", 4))


if __name__ == "__main__":
    test()
