
"""
字典+排序
"""

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count = collections.Counter(s)
        sortedCount = sorted(count.items(), key = lambda x:x[1], reverse=True)
        ans = 0
        for i in range(len(sortedCount)):
            if i < 9:
                ans += sortedCount[i][1]
            elif i <18:
                ans += 2*sortedCount[i][1]
            else:
                ans += 3*sortedCount[i][1]
        return ans


