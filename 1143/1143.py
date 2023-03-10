'''
看图
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for x in range(len(text2)+1)] for y in range(len(text1)+1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]