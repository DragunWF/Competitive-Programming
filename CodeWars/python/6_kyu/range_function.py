# https://www.codewars.com/kata/584ebd7a044a1520f20000d5/train/python

def range_function(start, step=None, stop=None) -> list[int]:
    output = []
    if step is None:
        for i in range(1, start + 1):  # Start becomes stop
            output.append(i)
    elif stop is None:
        for i in range(start, step + 1):  # Step becomes stop
            output.append(i)
    else:
        for i in range(start, stop + 1, step):
            output.append(i)
    return output
