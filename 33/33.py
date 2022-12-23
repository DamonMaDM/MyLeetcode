
"""
rotated sorted array 也可以直接 Binary Search
18,20 和 25，27可以合并一下
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] >= nums[0]:
                if target >= nums[0] and target < nums[m]:
                    r = m-1
                elif target >= nums[0] and target > nums[m]:
                    l = m+1
                else:
                    l = m+1
            else:
                if target <= nums[-1] and target > nums[m]:
                    l = m+1
                elif target <= nums[-1] and target < nums[m]:
                    r = m-1
                else:
                    r = m-1

        return -1