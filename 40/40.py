from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for x in range(target + 1)]
        dp[0].append(set()) #经典bottom up,0为botton设为空，所有的都从0开始走起

        candidates.sort()
        for j in range(len(candidates)):
            if candidates[j] > target:
                continue
            for i in range(candidates[j], target + 1):
                for s in dp[i - candidates[j]]:
                    # Each number in candidates may only be used once in the combination
                    if j not in s:  # 每个使用一次
                        copy_set = s.copy()
                        copy_set.add(j)
                        if len(dp[i]) == 0 or candidates[j - 1] != candidates[j] or j - 1 in s: #因为排序过所以相同的candidate只能和之前的叠加，不能重复
                            dp[i].append(copy_set)

        ans = []
        for s in dp[target]:

            l = []
            for index in s:
                l.append(candidates[index])
            ans.append(l)
        return ans


