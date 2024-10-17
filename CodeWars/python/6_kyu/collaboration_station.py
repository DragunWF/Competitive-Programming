# https://www.codewars.com/kata/57b31dc11fae8a4137000693/train/python

def split_message(message: str, count: int) -> list[str]:
    if count <= 0:
        return None
    messages = [[] for i in range(count)]
    for i, char in enumerate(message):
        messages[i % count].append(char)
        for j in range(count):
            if j != i % count:
                messages[j].append("-")
    return ["".join(received) for received in messages]
