
"""
经典DFS,BFS
dfs用recursive visited处理访问过的点
bfs用iteration queue（ First In First Out ），visited 处理访问过的点
"""

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # l = len(arr)
        # visted = [False for x in range(l)]

        # def dfs(index):
        #     if index < 0 or index >= l or visted[index]:
        #         return False
        #     if arr[index] == 0:
        #         return True
        #     visted[index] = True
        #     return dfs(index+arr[index]) or dfs(index-arr[index])
        # return dfs(start)

        l = len(arr)
        queue = [start]
        visted = [False for x in range(l)]
        while queue:
            node = queue.pop(0)
            if arr[node] == 0:
                return True
            if visted[node]:
                continue
            for i in [node+arr[node],node-arr[node]]:
                if i >= 0 and i < l:
                    queue.append(i)
            visted[node] = True
        return False