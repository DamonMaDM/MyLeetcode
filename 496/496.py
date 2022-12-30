
"""
Stack
Monotonic Stack
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        stack.append(nums2[0])
        for i in range(1,len(nums2)):
            x = nums2[i]
            while len(stack) != 0 and stack[-1] < x:
                n = stack.pop()
                dic[n] = x
            stack.append(x)
        while len(stack) != 0:
            dic[stack.pop()] = -1
        ans = []
        for i in nums1:
            ans.append(dic.get(i))
        return ans