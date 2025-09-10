# https://www.codewars.com/kata/57073869924f34185100036d

import random


def random_case(s: str) -> str:
    output = ""
    for char in s:
        chance = random.randint(1, 2)
        if chance == 1:
            output += char.lower()
        else:
            output += char.upper()
    return output


def test() -> None:
    # "lOReM ipSum DOloR SiT AmeT, cOnsEcTEtuR aDiPiSciNG eLIt"
    print(random_case("Lorem ipsum dolor sit amet, consectetur adipiscing elit"))


if __name__ == "__main__":
    test()
