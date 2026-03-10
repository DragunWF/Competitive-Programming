# https://www.codewars.com/kata/5b049d57de4c7f6a6c0001d7

def apparently(s: str) -> str:
    if not s:
        return ""
    words = s.split(" ")
    modified_sentence = []
    for i, word in enumerate(words):
        modified_sentence.append(word)
        if (word == "and" or word == "but") and (i + 1 <= len(words) and (i + 1 == len(words) or words[i + 1] != "apparently")):
            modified_sentence.append("apparently")
    return " ".join(modified_sentence)
