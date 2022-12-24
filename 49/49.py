
"""
一个用了collections, 一个只用{}

Table of Collections Content:

Counters
OrderedDict
DefaultDict
ChainMap
NamedTuple
DeQue
UserDict
UserList
UserString
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            if dic.get(tuple(sorted(s)))!=None:
                dic[tuple(sorted(s))].append(s)
            else:
                dic[tuple(sorted(s))] = [s]
        return dic.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for s in strs:
            dic[tuple(sorted(s))].append(s)
        return dic.values()