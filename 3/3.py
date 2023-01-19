
"""
经典Sliding Windows
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        start, end = 0 , 0
        ans = 0
        while end < len(s):
            if s[end] not in hash_set:
                hash_set.add(s[end])
            else:
                while start < end:
                    if s[start] == s[end]:
                        start += 1
                        break
                    hash_set.remove(s[start])
                    start += 1
            end += 1
            ans = max(end-start,ans)
        return ans