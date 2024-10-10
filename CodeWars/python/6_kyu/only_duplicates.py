# https://www.codewars.com/kata/5a1dc4baffe75f270200006b/train/python

def only_duplicates(st: str):
    output = ""
    for char in st:
        if st.count(char) > 1:
            output += char
    return output
