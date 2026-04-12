class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 1
        index2 = len(numbers)
        while index1 < len(numbers):
            while index2 > index1:
                if numbers[index1] + numbers[index2] == target:
                    return [numbers[index1], numbers[index2]]
                else:
                    index2 -=1
            index1 +=1