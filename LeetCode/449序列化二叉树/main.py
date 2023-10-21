from collections import deque


def list_to_tree(tree, nums, i):
    if i >= len(nums):
        return None

    if nums[i] == "N":
        return None
    else:
        tree = TreeNode(nums[i])
        tree.left = list_to_tree(tree.left, nums, 2 * i + 1)
        tree.right = list_to_tree(tree.right, nums, 2 * i + 2)

    return tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root) -> str:
        q = deque()
        q.append(root)
        temp_list = []

        while q:
            null_cnt = 0
            one_floor = []
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur:
                    one_floor.append("N")
                    null_cnt += 1
                    q.append(None)
                    q.append(None)
                else:
                    one_floor.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)

            if null_cnt == len(one_floor):
                break

            temp_list.extend(one_floor)

        res = ""
        for item in temp_list:
            res += str(item) + ","
        return res

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        """
        temp_list = data.split(",")[:-1]

        tree = list_to_tree(None, temp_list, 0)

        return tree


test_list = [1, 2, 2, "N", 4, 4, 3]
my_tree = list_to_tree(None, test_list, 0)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
tree = ser.serialize(my_tree)
ans = deser.deserialize(tree)
pass
