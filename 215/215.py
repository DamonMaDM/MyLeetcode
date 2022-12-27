
"""
两种方法
1. Priority Queue
2. QuickSork 变种
不要sort
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:

        def swap(i, j):
            m = nums[i]
            nums[i] = nums[j]
            nums[j] = m

        def partition(low, high, pivot_index):
            pivot = nums[pivot_index]
            swap(pivot_index, high)
            store_index = low  # 不等于0
            for i in range(low, high):
                if nums[i] < pivot:
                    swap(i, store_index)
                    store_index += 1
            swap(store_index, high)
            return store_index

        def select(l, r, k):
            if l == r:
                return
            pivot_index = random.randint(l, r)

            # find the pivot position in a sorted list
            pivot_index = partition(l, r, pivot_index)

            if pivot_index == k:
                return
            elif pivot_index > k:
                select(l, pivot_index - 1, k)  # 不用管前面的了
            else:
                select(pivot_index + 1, r, k)  # 不用管后面的了

        n = len(nums)
        select(0, n - 1, n - k)
        return nums[n - k]