
"""
非二叉树，树高计算
max([array])
O(N)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        elif root.children == []:
            return 1
        else:
            return max([self.maxDepth(i) for i in root.children])+1