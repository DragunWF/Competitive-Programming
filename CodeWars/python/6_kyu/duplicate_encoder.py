# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    string = [x.lower() for x in [*word]]
    return "".join(list(map(lambda x: ")" if string.count(x) > 1 else "(", string)))
