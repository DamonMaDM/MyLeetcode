
"""
镜像着DFS
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, n1, n2):
        if n1 == None and n2 == None:
            return True
        if n1 == None or n2 == None:
            return False
        return n1.val == n2.val and self.recursive(n1.left, n2.right) and self.recursive(n1.right, n2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.recursive(root, root)