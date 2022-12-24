
"""
更像数学题
"""

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeros(x):
            return x//5 + zeros(x//5) if x>0 else 0
        l = k
        r = 20*k
        while l<=r:
            m = (l+r)//2
            z = zeros(m)
            if z == k:
                return 5
            elif z<k:
                l = m+1
            else:
                r = m-1
        return 0