# https://www.codewars.com/kata/5268956c10342831a8000135/train/python


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def pre_order(node):
    values = []

    def traverse(node):
        if not node or node.data is None:
            return
        values.append(node.data)
        traverse(node.left)
        traverse(node.right)

    traverse(node)
    return values


def in_order(node):
    values = []

    def traverse(node):
        if not node or node.data is None:
            return
        traverse(node.left)
        values.append(node.data)
        traverse(node.right)

    traverse(node)
    return values


def post_order(node):
    values = []

    def traverse(node):
        if not node or node.data is None:
            return
        traverse(node.left)
        traverse(node.right)
        values.append(node.data)

    traverse(node)
    return values
