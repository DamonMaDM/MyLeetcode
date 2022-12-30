
"""
第10行loop的时候记得看一下算的是之前的group
所以最后想要再append一下
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groupCount = []
        count = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                groupCount.append(count)
                count = 1
            else:
                count += 1

        groupCount.append(count)

        ans = 0
        print(groupCount)
        for i in range(1, len(groupCount)):
            ans += min(groupCount[i - 1], groupCount[i])
        return ans