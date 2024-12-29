# https://www.codewars.com/kata/57262ca48565846f33001365/train/python

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def reverse_list(head: Node):
    return convert_to_linked_list(list(reversed(convert_to_list(head))))


def convert_to_list(head: Node) -> list[int]:
    values = []
    node = head
    while node:
        values.append(node.value)
        node = node.next
    return values


def convert_to_linked_list(values: list[int]) -> Node:
    if not values:
        return None
    head = Node(values[0], None)
    if len(values) == 1:
        return head
    node = Node(values[1], None)
    head.next = node
    for i in range(1, len(values)):
        node.value = values[i]
        if i != len(values) - 1:
            node.next = Node(values[i + 1], None)
        node = node.next
    return head


def test() -> None:
    linked_list = reverse_list(Node(1, Node(2, Node(3, None))))
    normal_list = convert_to_list(linked_list)
    print(normal_list)


if __name__ == "__main__":
    test()
