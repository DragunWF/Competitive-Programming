# https://www.codewars.com/kata/56ef9790740d30a7ff000199/train/python

from collections import deque


class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = [] if child_nodes is None else child_nodes


def tree_to_list(tree_root: Node) -> list:
    if not tree_root or isinstance(tree_root, list):
        return []

    output = []
    queue = deque([tree_root])

    while queue:
        current_node = queue.popleft()
        output.append(current_node.data)

        for child in current_node.child_nodes:
            if child:
                queue.append(child)

    return output


class TestCase:
    def __init__(self, tree_root: Node, expected: list):
        self.tree_root = tree_root
        self.expected = expected


def test() -> None:
    test_cases = [
        TestCase(Node(1, [Node(2, [Node(3), Node(4), Node(5)]), Node(3, [Node(7)])]), [1, 2, 3, 3, 4, 5, 7]),
        TestCase(Node(1, [Node(2, [Node(3), Node(4)]), Node(5, [Node(6)]), Node(7)]), [1, 2, 5, 7, 3, 4, 6]),
        TestCase(Node(1, [Node('a', [Node('A'), Node('B')]), Node('b', [Node('C'), Node('D', [Node(None)])])]), [
                 1, 'a', 'b', 'A', 'B', 'C', 'D', None])
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = tree_to_list(item.tree_root)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.tree_root}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
