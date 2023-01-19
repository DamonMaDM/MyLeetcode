
"""
同第三题，Sliding Windows
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        letter_counter = collections.Counter()
        left, right = 0, 0
        ans = 0
        while right < len(s):
            value = s[right]
            letter_counter[value] += 1

            while len(letter_counter) > 2:
                removed = s[left]
                if letter_counter[removed] == 1:
                    del letter_counter[removed]
                else:
                    letter_counter[removed] -= 1
                left += 1
            right += 1
            ans = max(ans, right-left)
        return ans
