# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    sentence, new_str = sentence.split(), []
    for line in sentence:
        new_line = [*line]
        if len(line) >= 5:
            new_line.reverse()
        new_str.append("".join(new_line))
    return ' '.join(new_str)
