class Solution:
    def countPairs(self, deliciousness) -> int:
        sum_res = []
        for i, item_i in enumerate(deliciousness):
            for j, item_j in enumerate(deliciousness):
                if i == j:
                    continue
                sum_res.append(item_i + item_j)
                
        pass


a = [1, 3, 5, 7, 9]
obj = Solution()
result = obj.countPairs(a)
pass