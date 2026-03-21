# https://www.codewars.com/kata/55d9f257d60c5fd98d00001b/train/python

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head: Node) -> Node:
    unique = []
    seen = set()

    current_node = head
    while current_node:
        if current_node.data not in seen:
            seen.add(current_node.data)
            unique.append(current_node.data)
        current_node = current_node.next

    return build_linked_list(unique)


def build_linked_list(values: list) -> Node:
    if not values:
        return None
    root = Node(values[0])
    if len(values) == 1:
        return root

    current_node = root
    next_node = None
    for i in range(1, len(values)):
        next_node = Node(values[i])
        current_node.next = next_node
        current_node = next_node
    return root


def test_display_linked_list(root: Node) -> None:
    displayed_list = []
    current_node = root
    while current_node:
        displayed_list.append(current_node.data)
        current_node = current_node.next
    return displayed_list


def test() -> None:
    result = remove_duplicates(build_linked_list([1, 2, 2, 3, 4, 5, 5]))
    print(test_display_linked_list(result))


if __name__ == "__main__":
    test()
