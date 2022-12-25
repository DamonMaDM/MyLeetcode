
"""
数数+循环
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        while n > 1:
            s2 = ''
            i = 0
            while i < len(s):
                j = i + 1
                while j < len(s) and s[i] == s[j]:
                    j += 1
                s2 = s2 + str(j - i) + s[i]
                i = j
            n -= 1
            s = s2

        return s