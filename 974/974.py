
"""
比较新颖的Prefix Sum
"""

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = []
        prefix.append(nums[0])
        #Prefix Sum of array
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]+nums[i])

        #Remain of (prefix Sum % k)
        # if remain[i] == remain[j], [i+1,j]这个subArray is divisible by k
        remain = []
        for i in range(len(nums)):
            remain.append((prefix[i]%k+k)%k)

        #为了不一个个去找，找subArray用counter
        counter = [0 for x in range(k)]
        counter[0] = 1
        ans = 0
        for i in range(len(nums)):
            ans += counter[remain[i]]
            counter[remain[i]] += 1
        return ans