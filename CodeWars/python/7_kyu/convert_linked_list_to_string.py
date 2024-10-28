# https://www.codewars.com/kata/582c297e56373f0426000098

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(node):
    values = []
    current_node = node
    while current_node != None:
        values.append(current_node.data)
        current_node = current_node.next
    values.append(None)
    return " -> ".join([str(i) for i in values])


def test():
    print(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))))


if __name__ == "__main__":
    test()
