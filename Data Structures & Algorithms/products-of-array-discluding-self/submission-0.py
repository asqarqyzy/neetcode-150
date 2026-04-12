class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            v = 1
            for j in range(len(nums)):
                if i != j:
                    v *= nums[j]
            l.append(v)
        return l