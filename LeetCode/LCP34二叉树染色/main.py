from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def max_value(self, root, k: int) -> int:
        dp = [1]
        q = deque()

        def backtrace(i,node):
            if node:
                q.append(node)





def list_to_tree(l_list, i, root):
    if i >= len(l_list):
        return None

    root = TreeNode(l_list[i])
    root.left = list_to_tree(l_list, 2 * i + 1, root.left)
    root.right = list_to_tree(l_list, 2 * i + 2, root.right)

    return root


obj = Solution()

tree_node = list_to_tree([5, 2, 3, 4], 0, None)

obj.max_value(tree_node, 2)
