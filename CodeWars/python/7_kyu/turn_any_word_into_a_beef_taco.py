# https://www.codewars.com/kata/59414b46d040b7b8f7000021/train/python

def tacofy(word: str) -> str:
    VOWELS = "aeiou"
    taco_map = {"t": "tomato", "l": "lettuce",
                "c": "cheese", "g": "guacamole", "s": "salsa"}
    output = ["shell"]

    for char in word.lower():
        if char in VOWELS:
            output.append("beef")
        elif char in taco_map:
            output.append(taco_map[char])
    output.append("shell")
    return output
