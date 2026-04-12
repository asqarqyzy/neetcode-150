class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import defaultdict
        num_set = set(nums)
        max_seq = 0
        for num in nums:
            if num-1 not in num_set:
                cur_seq = 0
                while num + cur_seq in num_set:
                    cur_seq += 1
                max_seq = max(cur_seq, max_seq)
        return max_seq