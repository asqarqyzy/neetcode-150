class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
        while index1 < len(numbers) - 1:
            curSum = numbers[index1] + numbers[index2]
            if curSum == target:
                return [index1 + 1, index2 + 1]
            elif curSum > target:
                index2 -= 1
            else:
                index1 += 1
        return None