# https://www.codewars.com/kata/5893933e1a88084be10001a3

from string import ascii_letters, digits


def validate(domain: str) -> bool:
    if len(domain) > 253:
        return False

    subdomains = domain.split(".")
    if len(subdomains) == 1 or len(subdomains) > 127:
        return False

    VALID_LEVEL_CHARS = f"{ascii_letters}{digits}-"
    for level in subdomains:
        if not level or len(level) > 63 or level.startswith("-") or level.endswith("-"):
            return False
        for char in level:
            if not char in VALID_LEVEL_CHARS:
                return False

    top_level_domain = subdomains[-1]
    if top_level_domain.isdigit():
        return False

    return True


def test() -> None:
    print(validate("codewars"))  # False
    print(validate("g.co"))  # True
    print(validate("codewars.com"))  # True
    print(validate('127.0.0.1'))  # False
    print(validate(".codewars.com"))  # False


if __name__ == "__main__":
    test()
