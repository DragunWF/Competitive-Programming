# https://www.codewars.com/kata/55d17ddd6d7868493e000074

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def append(listA: Node, listB: Node) -> Node:
    if not listA and not listB:
        return None
    if not listA and listB:
        return listB
    if listA and not listB:
        return listA
    head = listA
    current_node = head
    is_second_list = False
    while current_node:
        if not current_node.next and not is_second_list:
            current_node.next = listB
            is_second_list = True
        current_node = current_node.next
    return head


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
    list1 = build_linked_list([1, 2, 3])
    list2 = build_linked_list([4, 5, 6])
    print(test_display_linked_list(append(list1, list2)))


if __name__ == "__main__":
    test()
