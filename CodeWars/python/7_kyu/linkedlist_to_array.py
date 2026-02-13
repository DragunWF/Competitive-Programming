# https://www.codewars.com/kata/557dd2a061f099504a000088/train/python

# from preloaded import LinkedList

class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def list_to_array(node: LinkedList) -> list:
    output = []
    current_node = node
    while current_node:
        output.append(current_node.value)
        current_node = current_node.next
    return output
