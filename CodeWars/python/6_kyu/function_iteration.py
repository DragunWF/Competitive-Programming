# https://www.codewars.com/kata/54b679eaac3d54e6ca0008c9/train/python

def create_iterator(func, n):
    def iterator(initial_input):
        output, prev_output = 0, None
        prev_output = None
        for i in range(n):
            output = func(prev_output if prev_output else initial_input)
            prev_output = output
        return output
    return iterator
