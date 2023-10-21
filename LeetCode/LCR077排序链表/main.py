class ListNode:
    def __init__(self, val=0, node_next=None):
        self.val = val
        self.next = node_next


class Solution:
    def sort_list(self, head: ListNode) -> ListNode:
        res_list = []
        while head is not None:
            res_list.append(head.val)
            head = head.next

        res_list.sort()

        res_node = list_to_node(res_list, 0, None)
        return res_node


def list_to_node(l_list, i, node):
    if i >= len(l_list):
        return None
    node = ListNode(l_list[i])
    node.next = list_to_node(l_list, i + 1, node.next)
    return node


obj = Solution()

l_node = list_to_node([4, 2, 1, 3], 0, None)

obj.sort_list(l_node)
