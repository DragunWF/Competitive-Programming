# https://www.codewars.com/kata/583710f6b468c07ba1000017/train/python

def proofread(s: str) -> str:
    words = s.lower().split(" ")
    output = []
    for word in words:
        if "e" in word and "i" in word:
            output.append(switch_e_i(word))
            continue
        output.append(word)
    return capitalize_sentences(" ".join(output))


def switch_e_i(s: str):
    return s.replace("ie", "ei")


def capitalize_sentences(s: str):
    sentences = s.split(".")
    output = []
    for sentence in sentences:
        if sentence and sentence[0] == " ":
            char_arr = [*sentence.lower()]
            char_arr[1] = char_arr[1].upper()
            output.append("".join(char_arr))
        else:
            output.append(sentence.capitalize())
    return ".".join(output)


def test():
    # Not part of the solution, just testing
    s = "The neighbour's ceiling fell on his head. the weight of it crushed him to the ground."
    print(capitalize_sentences(s))
    print(proofread(
        "THe neIghBour's ceiLing FEll on His Head. The WiEght of It crusHed him To thE gROuNd."
    ))
    print(switch_e_i("iEght"))


if __name__ == "__main__":
    test()


def old_switch_e_i(s: str) -> str:
    i_index, e_index = None, None
    s = [*s]
    for i, char in enumerate(s):
        if char.lower() == "e":
            e_index = i
        elif char.lower() == "i":
            i_index = i
        if not i_index is None and not e_index is None:
            break
    if e_index > i_index:
        s[i_index], s[e_index] = s[e_index], s[i_index]
    return "".join(s)
