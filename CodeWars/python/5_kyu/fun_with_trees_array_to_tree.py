# https://www.codewars.com/kata/57e5a6a67fbcc9ba900021cd

from collections import deque
# from preloaded import Node


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def array_to_tree(arr: list[int]):
    if not arr:
        return

    root = Node(arr[0])
    queue = deque([root])
    i = 1
    while i < len(arr) and queue:
        current_node = queue.popleft()

        if i < len(arr):
            current_node.left = Node(arr[i])
            queue.append(current_node.left)
        i += 1

        if i < len(arr):
            current_node.right = Node(arr[i])
            queue.append(current_node.right)
        i += 1
    return root


def test() -> None:
    print(array_to_tree([17, 0, -4, 3, 15]))


if __name__ == "__main__":
    test()
