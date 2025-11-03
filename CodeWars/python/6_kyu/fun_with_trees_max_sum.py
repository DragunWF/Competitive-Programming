# https://www.codewars.com/kata/57e5279b7cf1aea5cf000359/python

# from preloaded import TreeNode

# This class comes from the preloaded module in the kata
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_sum(root: TreeNode) -> int:
    if not root:
        return 0

    route_sums = []

    def depth_first_traversal(node: TreeNode, current_sum: int):
        if not node:
            return

        current_sum += node.value
        depth_first_traversal(node.left, current_sum)
        depth_first_traversal(node.right, current_sum)

        if not node.left and not node.right:
            route_sums.append(current_sum)

    depth_first_traversal(root, 0)
    return max(route_sums)


def test() -> None:
    tree = TreeNode(5,
                    TreeNode(-22,
                             TreeNode(9),
                             TreeNode(50)),
                    TreeNode(11,
                             TreeNode(9),
                             TreeNode(2)))
    print(max_sum(tree))  # 33


if __name__ == "__main__":
    test()
