# https://www.codewars.com/kata/55f4a44eb72a0fa91600001e/train/python

str_list = []


def create_message(str=None):
    global str_list
    if str is None:
        output = [item for item in str_list]
        str_list = []
        return " ".join(output)
    str_list.append(str)
    return create_message
