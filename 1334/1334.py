"""
经典Floyd Warshall
点一点的最短距离
O(n**3)
"""

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[math.inf for x in range(n)] for y in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for e in edges:
            dp[e[0]][e[1]] = e[2]
            dp[e[1]][e[0]] = e[2]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][j] > dp[i][k]+dp[k][j]:
                        dp[i][j] = dp[i][k]+dp[k][j]
        ans = -1
        minConnect = math.inf
        for i in range(n):
            connect = 0
            for j in range(n):
                if dp[i][j] <= distanceThreshold:
                    connect+=1
            if connect<=minConnect:
                minConnect = connect
                ans = i
        return ans