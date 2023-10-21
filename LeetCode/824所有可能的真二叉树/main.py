import copy
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int):
        """遍历生成1<n<20所有的真二叉树，然后按n的要求返回"""
        res_table = []
        for _ in range(20):
            res_table.append([])
        res_table[0] = [list_to_tree(None, [0], 0)]

        for i in range(1, 20):
            if i % 2 != 0:
                continue

            res_pre = res_table[i - 2]
            res_table[i] = add_two_nodes(res_pre)

        return res_table[n-1]


def add_two_nodes(res_pre):
    temp_res = []

    for item in res_pre:
        q = deque()
        q.append(item)

        while q:
            cur = q.popleft()
            if cur.left and cur.right:
                q.append(cur.left)
                q.append(cur.right)
                continue

            temp_left = TreeNode(0)
            temp_right = TreeNode(0)
            cur.left = temp_left
            cur.right = temp_right
            temp_item = copy.deepcopy(item)
            cur.left = None
            cur.right = None
            temp_res.append(temp_item)

    return temp_res


def list_to_tree(tree, my_list, i):
    if i >= len(my_list):
        return None

    if not tree:
        tree = TreeNode(my_list[i])
    tree.left = list_to_tree(tree.left, my_list, 2 * i + 1)
    tree.right = list_to_tree(tree.right, my_list, 2 * i + 2)

    return tree


obj = Solution()
n = 3
result = obj.allPossibleFBT(n)
pass
