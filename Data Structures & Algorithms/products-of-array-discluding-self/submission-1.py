class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        v = 1
        for i in range(0, len(nums)):
            v *= nums[i]
            prefix.append(v)
        v = 1
        for i in range(len(nums)-1, -1, -1):
            v *= nums[i]
            suffix.append(v)
        suffix = suffix[::-1]
        result=[]
        for i in range(0, len(nums)):
            if i == 0:
                result.append(suffix[i+1])
            elif i == len(nums) - 1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1]*suffix[i+1])
        return result