# https://www.codewars.com/kata/582c5382f000e535100001a7/train/python

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linked_list_from_string(s: str) -> Node:
    if s == "None":
        return None
    elements = s.split(" -> ")
    head = Node(int(elements[0]))
    current = head
    for i in range(1, len(elements)):
        if elements[i] == "None":
            break
        current.next = Node(int(elements[i]))
        current = current.next
    return head
