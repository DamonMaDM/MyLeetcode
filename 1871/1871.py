
"""
Just prevent to start from repeated positions when performing BFS
"""

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        l = len(s)
        q = [0]
        #visted = [0 for x in range(l)]
        #visted[0] = True
        start_index = 1
        while q:
            i = q.pop(0)
            for j in range(max(start_index,i+minJump), min(i+maxJump+1, l)):
                if s[j] == '0':
                    if j == l-1:
                        return True
                    q.append(j)
                    #visted[j] = True
            start_index = i+maxJump+1 #如何避免的
        return False