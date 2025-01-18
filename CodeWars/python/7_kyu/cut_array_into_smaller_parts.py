# https://www.codewars.com/kata/58ac59d21c9e1d7dc5000150/train/python

def make_parts(arr: list, chunk_size: int) -> list:
    output = []
    chunk = []
    for i in range(len(arr)):
        chunk.append(arr[i])
        if (i + 1) % chunk_size == 0:
            output.append(chunk)
            chunk = []
    if chunk:
        output.append(chunk)
    return output
