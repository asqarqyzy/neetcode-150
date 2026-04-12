class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import defaultdict
        num_set = set(nums)
        res=[]
        for num in nums:
            max_seq=0
            if num-1 not in num_set:
                max_seq = 1
                while num + 1 in nums:
                    max_seq += 1
                    num +=1
            res.append(max_seq)
        return max(res)