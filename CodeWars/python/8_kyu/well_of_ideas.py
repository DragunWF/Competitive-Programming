# https://www.codewars.com/kata/57f222ce69e09c3630000212

def well(x):
    good = len([i for i in x if i == "good"])
    if not good:
        return "Fail!"
    return "Publish!" if good <= 2 else "I smell a series!"
