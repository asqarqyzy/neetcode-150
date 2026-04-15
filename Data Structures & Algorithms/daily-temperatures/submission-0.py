class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        i = 0
        counter = 1
        while i <= len(temperatures) - 1:
            if counter > len(temperatures) - 1 or i == len(temperatures) - 1:
                result.append(0)
                counter = len(result) + 1
            elif temperatures[counter] > temperatures[i]:
                result.append(counter - i)
                counter = len(result) + 1    
            else:
                counter += 1
            i = len(result)
        return result