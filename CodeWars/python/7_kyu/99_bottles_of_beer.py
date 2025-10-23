# https://www.codewars.com/kata/52a723508a4d96c6c90005ba/train/python

def sing():
    bottles = 99
    song = []
    while bottles > 0:
        bottle_word = get_bottle_word(bottles)
        song.append(
            f"{bottles} {bottle_word} of beer on the wall, {bottles} {bottle_word} of beer."
        )
        bottles -= 1
        bottle_word = get_bottle_word(bottles)
        if bottles == 0:
            song.append(
                f"Take one down and pass it around, no more bottles of beer on the wall.")
        else:
            song.append(
                f"Take one down and pass it around, {bottles} {bottle_word} of beer on the wall.")
    song.append("No more bottles of beer on the wall, no more bottles of beer.")
    song.append(
        "Go to the store and buy some more, 99 bottles of beer on the wall."
    )
    return song


def get_bottle_word(bottles: int) -> str:
    return "bottle" if bottles == 1 else "bottles"


def test() -> None:
    print(sing())


if __name__ == "__main__":
    test()
