# https://www.codewars.com/kata/69347c0454f16273e13b56e8

def pick(preferred: list[str], blacklisted: list[str], options: list[tuple[str, int]]) -> str:
    preferred_options = {}
    neutral_options = {}
    for skill, percentage in options:
        if not skill in blacklisted:
            if skill in preferred:
                preferred_options[percentage] = skill
            else:
                neutral_options[percentage] = skill
    if preferred_options:
        return get_letter_choice(preferred_options, options)
    if neutral_options:
        return get_letter_choice(neutral_options, options)
    return "D"


def get_letter_choice(chosen_options: dict, all_options: list[tuple[str, int]]) -> str:
    letter_choices = ("A", "B", "C")
    max_percentage = max(chosen_options.keys())
    chosen_skill = chosen_options[max_percentage]
    return letter_choices[get_option_index(chosen_skill, max_percentage, all_options)]


def get_option_index(skill: str, percentage: int, options: list[tuple[str, int]]) -> int:
    for i, option in enumerate(options):
        if option[0] == skill and percentage == option[1]:
            return i


def test() -> None:
    # Expected: C
    print(pick(
        {"attack", "defense"},
        {"luck"},
        (("luck", 25), ("speed", 20), ("defense", 15))
    ))

    # Expected: B
    print(pick(
        {'damage', 'agility', 'speed', 'attack'},
        set(),
        (('agility', 36), ('agility', 84), ('endurance', 29))
    ))


if __name__ == "__main__":
    test()
