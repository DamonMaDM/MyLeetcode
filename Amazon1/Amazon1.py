
"""
较为简单的Amazon
"""

from typing import List


def max_profit(k: int, profit: List[int]) -> int:
    n = len(profit)
    half = n//2
    if k == half:
        return sum(profit)
    sumK = 0
    for i in range(k): #初始值
        sumK += profit[i]+profit[i+half]
    ans = sumK
    for i in range(1,half):
        sumK = sumK - profit[i-1]-profit[i+half-1]+profit[i+k]+profit[(i+k+half)%n]
        ans = max(ans,sumK)
    return ans

print(max_profit(2,[1,5,1,3,7,-3]))
print(max_profit(1,[-6,3,6,-3]))


