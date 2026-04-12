class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dict_strs = defaultdict(list)
        for s in strs:
            sorted_s = tuple(sorted(s))
            dict_strs[sorted_s].append(s)
        return list(dict_strs.values())