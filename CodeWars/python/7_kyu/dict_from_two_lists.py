# https://www.codewars.com/kata/5533c2a50c4fea6832000101

def create_dict(keys, values):
    output = {}
    for i in range(len(keys)):
        output[keys[i]] = values[i] if i < len(values) else None
    return output
