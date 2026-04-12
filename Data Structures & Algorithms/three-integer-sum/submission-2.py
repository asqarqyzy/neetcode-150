class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        for i1 in range(len(sorted_nums) - 1, 0, -1):
            target = (-1) * sorted_nums[i1]
            i2 = 0
            i3 = i1 - 1
            while i2 < i3:
                curSum = sorted_nums[i2] + sorted_nums[i3]
                triplet = [sorted_nums[i1], sorted_nums[i2], sorted_nums[i3]]
                if curSum == target:
                    if triplet not in result:
                        result.append(triplet)
                    break
                elif curSum > target:
                    i3 -= 1
                else:
                    i2 += 1
        return result
