# https://www.codewars.com/kata/58279e13c983ca4a2a00002a/train/python

def greet_developers(lst: list[dict]):
    output = []
    for item in lst:
        item["greeting"] = f"Hi {item['firstName']}, what do you like the most about {item['language']}?"
        output.append(item)
    return output
