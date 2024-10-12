# https://www.codewars.com/kata/5898b4b71d298e51b600014b/train/python

def sort_the_inner_content(sentence: str) -> str:
    words = sentence.split(" ")
    output = []
    for word in words:
        if len(word) <= 2:
            output.append(word)
            continue
        inner_content = word[1:len(word) - 1]
        output.append(f"{word[0]}{''.join(sorted(inner_content, reverse=True))}{word[-1]}")
    return " ".join(output)