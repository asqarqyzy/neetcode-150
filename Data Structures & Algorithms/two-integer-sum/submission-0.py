class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i in range(len(nums)):
            dict_nums[target - nums[i]] = i
            if nums[i] in dict_nums:
                if dict_nums.get(nums[i]) != i:
                    return [dict_nums.get(nums[i]), i]