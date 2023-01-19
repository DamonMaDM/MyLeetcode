
"""
经典题
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #第一种情况，Top down，开始remin是满的，减小中找最小
        # @lru_cache(None) #让cache没限制的增长
        # def dfs(rem):
        #     if rem < 0:
        #         return -1
        #     if rem == 0:
        #         return 0
        #     min_coin = float('inf')
        #     for coin in coins:
        #         result = dfs(rem-coin)
        #         if result != -1:
        #             min_coin = min(min_coin, result+1)
        #     return min_coin if min_coin != float('inf') else -1
        # return dfs(amount)

        #第二种情况，Bottom up, 先全是inf，再一个个加上去，加的时候便利之前最小的
        dp = [float('inf')]*(amount+1)
        #只有和零增的时候才算数
        dp[0] = 0
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1