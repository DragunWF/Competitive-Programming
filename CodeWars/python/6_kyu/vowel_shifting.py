# https://www.codewars.com/kata/577e277c9fb2a5511c00001d

def vowel_shift(text: str, n: int) -> str:
    if not text or n == 0:
        return text

    VOWELS = "aeiouAEIOU"
    vowel_indicies = []
    vowel_characters = []
    for i, char in enumerate(text):
        if char in VOWELS:
            vowel_indicies.append(i)
            vowel_characters.append(char)

    output = [*text]
    shifted_vowel_characters = shift_list(vowel_characters, n)
    for i in range(len(shifted_vowel_characters)):
        output[vowel_indicies[i]] = shifted_vowel_characters[i]
    return "".join(output)


def shift_list(vowel_list: list[str], n: int) -> list[str]:
    LIST_LENGTH = len(vowel_list)
    output = ["" for i in range(LIST_LENGTH)]
    for i in range(LIST_LENGTH):
        output[(i + n) % LIST_LENGTH] = vowel_list[i]
    return output


def test() -> None:
    test_case = "This is a test!"
    print(shift_list(["a", "b", "c"], 1))

    # "Thes is i tast!"
    print(vowel_shift(test_case, 1))

    # "This as e tist!
    print(vowel_shift(test_case, 3))


if __name__ == "__main__":
    test()
