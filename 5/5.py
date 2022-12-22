
"""
开始分为 aa,bab 两种类型
1. dp[i][i+1] == 1
2. dp[i+1][j-1] == 1 (之前就得是True) and dp[i][j] == 1（首尾也相同） 这里i+k-1==j
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        max_length = 1
        start = 0
        for i in range(len(s)):
            dp[i][i] = True
            start = i
        for i in range(len(s)-1):
            if(s[i] == s[i+1]):
                dp[i][i+1] = True
                max_length = 2
                start = i
        k = 3
        while k<= len(s):
            for i in range(len(s)-k+1):
                j = i+k-1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    start = i
                    max_length = k
                i+=1
            k+=1
        return s[start:start+max_length]