
"""
典型DFS题，可以多看看
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = [[0 for i in range(n)] for j in range(m)]
        atlantic = [[0 for i in range(n)] for j in range(m)]

        def dfs(i, j, reachable):
            reachable[i][j] = 1
            for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                new_i = i + x
                new_j = j + y
                if new_i < 0 or new_i > m - 1 or new_j < 0 or new_j > n - 1:
                    continue
                elif heights[new_i][new_j] < heights[i][j]:
                    continue
                elif reachable[new_i][new_j] == 1:
                    continue
                dfs(new_i, new_j, reachable)

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        for i in range(n):
            dfs(0, i, pacific)
            dfs(m - 1, i, atlantic)
        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        return ans
