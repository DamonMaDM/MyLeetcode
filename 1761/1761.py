
"""
O(n**3) 三次循环找Trios， Brute Force
应该会有更好的解法
但vertex 数小于400，可以brute force
"""

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        gMatrix = [[0 for x in range(n+1)] for y in range(n+1)]
        edgesCount = [0]*(n+1)
        ans = n*(n-1)/2
        for e in edges:
            v1 = e[0]
            v2 = e[1]
            edgesCount[v1] += 1
            edgesCount[v2] += 1
            gMatrix[v1][v2] = 1
            gMatrix[v2][v1] = 1
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if gMatrix[i][j] != 1:
                    continue
                for k in range(j+1,n+1):
                    if gMatrix[i][k] == 1 and gMatrix[j][k] == 1:
                        degree = edgesCount[i]+edgesCount[j]+edgesCount[k]-6
                        ans = min(ans, degree)
        return ans if ans != n*(n-1)/2  else -1