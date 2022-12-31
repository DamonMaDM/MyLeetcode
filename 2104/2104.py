
"""
用两次Monotonic Stack
第一次 Monotonic increasing Stack
第二次 Monotonic decreasing Stack
"""

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        stack = []
        min_sum = 0
        for i in range(len(nums) + 1): #increasing stack
            while len(stack) != 0 and (i == len(nums) or nums[i] < nums[stack[-1]]):
                middle = stack.pop()
                l = -1 if not stack else stack[-1]
                min_sum += nums[middle] * (middle - l) * (i - middle)
            stack.append(i)

        stack.clear()
        max_sum = 0
        for i in range(len(nums) + 1): #decreasing stack
            while len(stack) != 0 and (i == len(nums) or nums[i] > nums[stack[-1]]):
                middle = stack.pop()
                l = -1 if not stack else stack[-1]
                max_sum += nums[middle] * (middle - l) * (i - middle)
            stack.append(i)

        return max_sum - min_sum