class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left) # 左右对称节点递归判断！！！

        res = recur(root.left, root.right)
        return res


def list_to_tree(tree, nums, i):
    if i >= len(nums):
        return None

    tree = TreeNode(nums[i])
    tree.left = list_to_tree(tree.left, nums, 2 * i + 1)
    tree.right = list_to_tree(tree.right, nums, 2 * i + 2)

    return tree


obj = Solution()
test_list = [1, 2, 2, 3, 4, 4, 3]
tset_res = True

my_tree = list_to_tree(None, test_list, 0)
result = obj.isSymmetric(my_tree)
assert result == tset_res
pass
