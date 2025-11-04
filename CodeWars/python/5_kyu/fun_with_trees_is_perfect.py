# https://www.codewars.com/kata/57dd79bff6df9b103b00010f/train/python

# from preloaded import TreeNode
from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_perfect(root: TreeNode) -> bool:
    if root is None:
        return True

    queue = deque([root])
    depth_of_first_leaf = -1
    depth = 0
    while queue:
        level_size = len(queue)  # Number of nodes at current level

        for _ in range(level_size):
            node: TreeNode = queue.popleft()

            if not node.left and not node.right:
                if depth_of_first_leaf == -1:
                    depth_of_first_leaf = depth
                elif depth_of_first_leaf != depth:
                    return False
            elif (node.left and not node.right) or (node.right and not node.left):
                return False
            else:
                queue.append(node.left)
                queue.append(node.right)

        depth += 1
    return True


def test() -> None:
    print(is_perfect(TreeNode('A',
                              TreeNode('B'),
                              TreeNode('C')
                              )))  # True

    balanced_nonperfect = TreeNode('A',
                                   TreeNode('B',
                                            TreeNode('D'),
                                            ),
                                   TreeNode('C',
                                            TreeNode('F'),
                                            )
                                   )
    print(is_perfect(balanced_nonperfect))  # False

    full_nonperfect = TreeNode('A',
                               TreeNode('B',
                                        TreeNode('D'),
                                        TreeNode('E')
                                        ),
                               TreeNode('C')
                               )
    print(is_perfect(full_nonperfect))  # False

    perfect_2_levels = TreeNode('A',
                                TreeNode('B',
                                         TreeNode('D'),
                                         TreeNode('E')
                                         ),
                                TreeNode('C',
                                         TreeNode('F'),
                                         TreeNode('G')
                                         )
                                )
    print(is_perfect(perfect_2_levels))  # True


if __name__ == "__main__":
    test()
