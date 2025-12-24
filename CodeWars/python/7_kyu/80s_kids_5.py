# https://www.codewars.com/kata/5667525f0f157f7a0a000004

def bucket_of(said: str) -> str:
    said = said.strip().lower()
    has_water_word = has_word(["water", "wet", "wash"], said)
    has_slime_word = has_word(["slime", "i don't know"], said)
    if has_water_word and has_slime_word:
        return "sludge"
    if not has_water_word and not has_slime_word:
        return "air"
    return "water" if has_water_word else "slime"


def has_word(words: list[str], said: str) -> bool:
    for word in words:
        if word in said:
            return True
    return False


def test() -> None:
    print(bucket_of("wet water"))


if __name__ == "__main__":
    test()
