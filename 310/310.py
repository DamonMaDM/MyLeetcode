
"""
第一种方法是559的遍历形似O(N**2), 时间复杂度过大
第二种是减去每次leaf值为1的点，一圈圈类似BFS缩，最后缩成1个或2个点
"""

# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         edgesMatrix = [[0 for x in range(n)]for y in range(n)]
#         for e in edges:
#             edgesMatrix[e[0]][e[1]] = 1
#             edgesMatrix[e[1]][e[0]] = 1
#         visited = [0]*n
#         treeHeight = [0]*n
#         ans = []
#         minHeight = n+1
#         def dfs(i,current,h):
#             visited[current] = 1
#             treeHeight[i] = max(treeHeight[i],h)
#             for j in range(n):
#                 if visited[j] == 0 and edgesMatrix[current][j] == 1:
#                     dfs(i,j,h+1)
#             visited[current] = 0


#         for i in range(n):
#             dfs(i,i,1)
#             if treeHeight[i] < minHeight:
#                 ans.clear()
#                 minHeight = treeHeight[i]
#                 ans.append(i)
#             elif treeHeight[i] == minHeight:
#                 ans.append(i)
#         return ans


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [x for x in range(n)]
        adjacency = [set() for x in range(n)] #用set节约时间
        for start, end in edges:
            adjacency[start].add(end)
            adjacency[end].add(start)
        leaves = []
        for i in range(n):
            if len(adjacency[i]) == 1:
                leaves.append(i)
        nodes = n
        while nodes > 2:
            nodes -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = adjacency[leaf].pop()
                adjacency[neighbor].remove(leaf)
                if len(adjacency[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves