# https://www.codewars.com/kata/59bc0059bf10a498a6000025/train/python

def mutate_my_strings(s1: str, s2: str) -> str:
    char_list_s1 = [*s1]
    output = [s1]
    for i, char in enumerate(s2):
        if char_list_s1[i] == s2[i]:
            continue

        char_list_s1[i] = char
        converted_str = "".join(char_list_s1)
        output.append(converted_str)

        if converted_str == s2:
            break
        
    return "\n".join(output) + "\n"
