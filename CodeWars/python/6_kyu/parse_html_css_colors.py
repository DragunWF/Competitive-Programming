# https://www.codewars.com/kata/58b57ae2724e3c63df000006

# Predefined constant in the CodeWars kata
PRESET_COLORS = {"LimeGreen":  "#32CD32"}


def parse_html_color(color: str) -> str:
    hexadecimal = None
    if not color.startswith("#"):
        hexadecimal = PRESET_COLORS[color.lower()]
    else:
        hexadecimal = color

    if len(hexadecimal) == 7:
        red = int(hexadecimal[1:3], 16)
        green = int(hexadecimal[3:5], 16)
        blue = int(hexadecimal[5:7], 16)
        return {"r": red, "g": green, "b": blue}
    red = int(f"{hexadecimal[1]}{hexadecimal[1]}", 16)
    green = int(f"{hexadecimal[2]}{hexadecimal[2]}", 16)
    blue = int(f"{hexadecimal[3]}{hexadecimal[3]}", 16)
    return {"r": red, "g": green, "b": blue}


def test() -> None:
    print(parse_html_color('#80FFA0'))   # => {'r': 128, 'g': 255, 'b': 160}
    print(parse_html_color('#3B7'))      # => {'r': 51,  'g': 187, 'b': 119}
    print(parse_html_color('LimeGreen'))  # => {'r': 50,  'g': 205, 'b': 50 }


if __name__ == "__main__":
    test()
