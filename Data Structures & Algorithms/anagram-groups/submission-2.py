class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dict_strs = defaultdict(list)
        for s in strs:
            alphabet = [0] * 26
            for alpha in s:
                alphabet[ord(alpha) - ord("a")] += 1
            dict_strs[tuple(alphabet)].append(s)
        return list(dict_strs.values())