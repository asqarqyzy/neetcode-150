class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dict_nums:
                return [dict_nums[diff], i]
            dict_nums[num] = i