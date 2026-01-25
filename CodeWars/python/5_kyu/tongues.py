# https://www.codewars.com/kata/52763db7cffbc6fe8c0007f8/train/python

def tongues(code: str) -> str:
    SPECIAL_VOWELS = 'aiyeou'
    CONSONANTS = 'bkxznhdcwgpvjqtsrlmf'
    output = []
    for char in code:
        if char.lower() in SPECIAL_VOWELS:
            output.append(encrypt_char(char, 3, SPECIAL_VOWELS))
        elif char.lower() in CONSONANTS:
            output.append(encrypt_char(char, 10, CONSONANTS))
        else:
            output.append(char)
    return "".join(output)


def encrypt_char(char: str, key: int, pool: str) -> str:
    new_index = (pool.index(char.lower()) + key) % len(pool)
    letter = pool[new_index]
    return letter.upper() if char.isupper() else letter


def test() -> None:
    # Expected: Ita dotf ni dyca nsaw ecc.
    print(tongues("One ring to rule them all."))


if __name__ == "__main__":
    test()
