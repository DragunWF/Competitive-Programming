# https://www.codewars.com/kata/513fa1d75e4297ba38000003/train/python

def flatten(*args):
    output = []
    def traverse(arr, i):
        if type(arr[i]) == list:
            if arr[i]:   
                traverse(arr[i], 0)
        else:
            output.append(arr[i])
        if i < len(arr) - 1:
            traverse(arr, i + 1)
    if len(args) > 0:
        traverse(args, 0)
    return output

def test() -> None:
    # Not part of the solution, just testing
    print(flatten(1, [2, 3], 4, 5, [6, [7]]))

if __name__ == "__main__":
    test()