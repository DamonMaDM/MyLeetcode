
"""
找连通图数量，可以改变成找最大连通图。。。。。
"""

class Solution:
    def dfs(self, visited, i, edgesMatrix, n):
        visited[i] = 1
        for j in range(n):
            if edgesMatrix[i][j] == 1 and visited[j] != 1:
                self.dfs(visited, j, edgesMatrix, n)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [0]*n
        edgesMatrix = [[0 for i in range(n)] for j in range(n)]
        for e in edges:
            edgesMatrix[e[0]][e[1]] = 1
            edgesMatrix[e[1]][e[0]] = 1
        ans = 0
        for i in range(n):
            if visited[i] != 1:
                ans += 1
                self.dfs(visited, i, edgesMatrix, n)
        return ans