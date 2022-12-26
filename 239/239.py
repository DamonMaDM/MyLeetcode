
"""
sliding window max典型
window 有固定size
第二种写法最规范
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        n = len(nums)
        ans = []
        if k==1:
            return nums
        for i in range(n):
            if i > k-1 and dq[0] == nums[i-k]:
                dq.popleft()
            while dq and dq[-1] < nums[i]:
                dq.pop()
            dq.append(nums[i])
            if i >=k-1:
                ans.append(dq[0])
        return ans



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        n = len(nums)
        ans = []
        l, r = 0, 0
        if k==1:
            return nums
        while r < n:
            while dq and dq[-1] < nums[r]:
                dq.pop()
            dq.append(nums[r])
            if r-l == k-1:
                ans.append(dq[0])
                if dq[0] == nums[l]:
                    dq.popleft()
                l += 1
            r += 1
        return ans