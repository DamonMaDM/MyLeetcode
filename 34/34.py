
"""
找范围，改变了if Middle = target的代码，去找的是最前面一个或者最后面一个
"""

class Solution:
    def bs(self, nums, target, findFirst):
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                if findFirst:
                    if m == 0 or nums[m-1]!=target:
                        return m
                    else:
                        r = m -1;
                else:
                    if m==len(nums)-1 or nums[m+1] != target:
                        return m
                    else:
                        l = m+1
            elif nums[m]>target:
                r = m-1
            else:
                l = m+1
        return -1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        ans.append(self.bs(nums, target, True))
        ans.append(self.bs(nums,target,False))
        return ans