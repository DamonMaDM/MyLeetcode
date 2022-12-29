
"""
关键看https://leetcode.com/problems/make-array-strictly-increasing/solutions/377403/python-dp-solution-with-explanation/?orderBy=most_votes
的解说，关键在于24、26行两种情况的讨论
"""

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(arr2)
        print(arr2)
        n1 = len(arr1)
        n2 = len(arr2)
        dp = [[n2+1 for i in range(n2+1)] for j in range(n1)]
        dp[0][0] = 0
        loc = bisect.bisect_right(arr2,-1)
        if loc < len(arr2):
            dp[0][loc+1] = min(dp[0][loc+1],1)
        for i in range(1,n1):
            x = arr1[i]
            for j in range(n2+1):
                if dp[i-1][j] != n2+1:
                    if j == 0:
                        if arr1[i-1] < x :#For example, we have state (5,0), and now i=7, we say um, it looks good so far we can generate a new state (7,0) because 7>5 it is increasing. No need to pick up a number from arr2
                            dp[i][0] = min(dp[i][0], dp[i-1][j]) #这一项直接沿用arr1[i]的值，所以把结果都放在[i][0]上
                        loc = bisect.bisect_right(arr2,arr1[i-1]) #找通路最近的大值
                        if loc < len(arr2):  #这一项放的位置根据前一个有效通路来，所以结果放在新的通路上[i][loc+1]
                            dp[i][loc+1] = min(dp[i][loc+1],dp[i-1][j]+1)
                    else:
                        if arr2[j-1] < x:
                            dp[i][0] = min(dp[i][0], dp[i-1][j])
                        loc = bisect.bisect_right(arr2,arr2[j-1])
                        if loc < len(arr2):
                            dp[i][loc+1] = min(dp[i][loc+1], dp[i-1][j]+1)

        ans = n2+1
        for j in range(n2+1):
            if dp[n1-1][j] < ans:
                ans = dp[n1-1][j]
        return -1 if ans == n2+1 else ans
