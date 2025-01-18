# https://www.codewars.com/kata/57212c55b6fa235edc0002a2/train/python

def common_ground(s1: str, s2: str) -> str:
    if not s1 and not s2:
        return "death"
    common = []
    s1_words, s2_words = s1.split(' '), s2.split(' ')
    for word in s2_words:
        if word in s1_words and not word in common:
            common.append(word)
    return " ".join(common) if common else "death"
