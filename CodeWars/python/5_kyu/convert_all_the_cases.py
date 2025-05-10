# https://www.codewars.com/kata/59be8c08bf10a49a240000b1/train/python

def change_case(identifier: str, target_case: str) -> str:
    if not identifier:
        return ""

    is_kebab = "-" in identifier
    is_camel = any([char.isupper() for char in identifier])
    is_snake = "_" in identifier

    if [is_kebab, is_camel, is_snake].count(True) != 1:
        return None

    if target_case == "snake":
        return identifier.replace("-", "_") if is_kebab else convert_camel_to_snake(identifier)
    elif target_case == "camel":
        return convert_to_camel(identifier, is_kebab)
    elif target_case == "kebab":
        return identifier.replace("_", "-") if is_snake else convert_camel_to_kebab(identifier)

    return None


def convert_to_camel(s: str, is_kebab: bool) -> str:
    output_words = []
    words = s.split("-" if is_kebab else "_")
    output_words.append(words[0])
    for i in range(1, len(words)):
        output_words.append(words[i].capitalize())
    return "".join(output_words)


def convert_camel_to_snake(s: str) -> str:
    return convert_camel_to_other_case(s, True)


def convert_camel_to_kebab(s: str) -> str:
    return convert_camel_to_other_case(s, False)


def convert_camel_to_other_case(s: str, is_snake: bool) -> str:
    words = []
    word = ""
    for char in s:
        if char.isupper():
            words.append(word)
            word = ""
        word += char.lower()
    words.append(word)
    return ("_" if is_snake else "-").join(words)


def test() -> None:
    print(change_case("snakeCase", "snake"))
    print(change_case("some-lisp-name", "camel"))
    print(change_case("map_to_all", "kebab"))
    print(change_case("doHTMLRequest", "kebab"))
    print(change_case("invalid-inPut_bad", "kebab"))

    print(convert_camel_to_kebab("doHTMLRequest"))


if __name__ == "__main__":
    test()
