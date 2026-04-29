# https://www.codewars.com/kata/650017e142964e000f19cac3/train/python

def empty_values(data: list) -> list:
    output = []
    for item in data:
        if type(item) is int:
            output.append(0)
        elif type(item) is str:
            output.append("")
        elif type(item) is float:
            output.append(0.0)
        elif type(item) is bool:
            output.append(False)
        elif type(item) is list:
            output.append([])
        elif type(item) is tuple:
            output.append(tuple([]))
        elif type(item) is dict:
            output.append({})
        elif type(item) is set:
            output.append(set())
        else:
            output.append(item)
    return output
