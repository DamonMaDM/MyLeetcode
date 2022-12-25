
"""
二分法找square root
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l = 2
        r = x//2
        while l<=r:
            m = (l+r)//2
            num = m*m
            if num == x:
                return m
            elif num > x:
                r = m-1
            else:
                l = m+1
        return r