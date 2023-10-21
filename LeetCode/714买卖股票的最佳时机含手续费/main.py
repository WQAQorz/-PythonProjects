class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        """
        tips：每个阶段都需要钱变多才会进行交易，贪婪思想，总收益最优就是所有的局部最优加起来。
        每天的操作只有买和卖，取决于前一天手上是否持有股票，通过动态规划直接遍历所有持股状态。
        状态转移方程为：第i+1天的状态由第i天的状态转移而来，配合买卖费用即可，参考第12/13行。
        """

        n = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]


obj = Solution()

a = [1, 3, 2, 8, 4, 9]
b = 2

obj.maxProfit(a, b)
pass
