
"""
关键：dp[i] = min(dp[max(i-1,0)]+costs[0],dp[max(i-7,0)]+costs[1],dp[max(i-30,0)]+costs[2])
"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_duration = [1,7,30]
        largest_day = days[-1]
        dp = [0]*(largest_day+1)
        day_set = set(days)
        for i in range(1,largest_day+1):
            if i in day_set:
                dp[i] = min(dp[max(i-1,0)]+costs[0],dp[max(i-7,0)]+costs[1],dp[max(i-30,0)]+costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[largest_day]