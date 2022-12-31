
"""
简单的sliding window
"""

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        n = len(arr)
        kSum = 0
        for i in range(k):
            kSum += arr[i]
        ans += 0 if kSum/k < threshold else 1
        for i in range(1,n-k+1):
            kSum = kSum - arr[i-1] +arr[i+k-1]
            ans += 0 if kSum/k < threshold else 1
        return ans