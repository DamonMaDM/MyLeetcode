
"""
纯用排序，不能用字典，identifier有重复的
(0, content, identifier)优先级从大到小写
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(x):
            identifier, content = x.split(' ', maxsplit = 1)
            return (0, content, identifier) if content.islower() else (1,) #最后顺序从下到大，（）里面优先级从大到小
        return sorted(logs, key = get_key)