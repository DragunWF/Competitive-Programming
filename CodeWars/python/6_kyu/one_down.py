# https://www.codewars.com/kata/56419475931903e9d1000087

def one_down(txt: str) -> str:
    if type(txt) is not str:
        return "Input is not a string"
    KEY = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    decrypted = ""
    for char in txt:
        if not char in KEY:
            decrypted += char
            continue
        decrypted_char = KEY[(KEY.index(char) - 1) % len(KEY)]
        # To take care of edge cases for "Aa" and "Zz"
        if char.isupper():
            decrypted += decrypted_char.upper()
        else:
            decrypted += decrypted_char.lower()
    return decrypted


def test() -> None:
    # Expected: Hello
    print(one_down("Ifmmp"))
    # Expected: The trick to this kata is simple
    print(one_down("Uif usjdl up uijt lbub jt tjnqmf"))
    # Expected: WhAt AbOuT cRaZy TeXt
    print(one_down("XiBu BcPvU dSbAz UfYu"))


if __name__ == "__main__":
    test()
