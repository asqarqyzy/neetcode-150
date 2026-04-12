class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
            if nums_dict[num] > 1:
                return True
        return False
        