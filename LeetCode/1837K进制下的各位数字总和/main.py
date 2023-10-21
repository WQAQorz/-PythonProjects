class Solution:
    def sumBase(self, n: int, k: int) -> int:
        temp = n
        res = []


        while temp >= k:
            digit = temp % k
            res.append(digit)
            temp = temp // k
        res.append(temp)

        return sum(res)


obj = Solution()
a = 10
b = 10
result = obj.sumBase(a, b)
pass
