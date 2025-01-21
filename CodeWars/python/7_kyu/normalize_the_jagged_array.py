# https://www.codewars.com/kata/6329437e3b59a10065e63a2f/train/python

def normalize(matrix: list, fill_value=None) -> list:
    if not matrix:
        return []
    
    output = []
    max_len = max(len(arr) for arr in matrix)
    for arr in matrix:
        row = []
        for i in range(max_len):
            row.append(arr[i] if i < len(arr) else fill_value)
        output.append(row)
        
    return output