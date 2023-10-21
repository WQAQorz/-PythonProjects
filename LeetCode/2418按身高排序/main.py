class Solution:
    def sortPeople(self, names, heights):
        temp_dict = dict(zip(heights,names))

        heights.sort(reverse=1)

        res = []
        for height in heights:
            res.append(temp_dict[height])

        return res

a = ["Mary", "John", "Emma"]
b = [180, 165, 170]
obj = Solution()
obj.sortPeople(a, b)
