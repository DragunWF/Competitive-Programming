# https://www.codewars.com/kata/5168b125faced29f66000005/train/python

def solution(full_text: str, search_text: str) -> str:
    if not search_text:
        return len(full_text) + 1
    count = 0
    current_substring = ""
    for char in full_text:
        current_sublen = len(current_substring)
        if char == search_text[current_sublen]:
            current_substring += char
        else:
            current_substring = ""
        if current_substring == search_text:
            count += 1
            current_substring = ""
    return count
