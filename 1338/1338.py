
"""
counter dictionary + sorted
字典加排序
"""

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        s = sorted(count.items(), key = lambda x:x[1], reverse=True)
        print(s)
        n = len(arr)
        ans = 0
        removed = 0
        while ans < len(count):
            removed += s[ans][1]
            if removed*2 >= n:
                return ans+1
            ans +=1
        return ans