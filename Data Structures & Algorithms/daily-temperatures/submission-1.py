class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for working_i, working_t in enumerate(temperatures):

            while stack and stack[-1][1] < working_t:
                stack_ind, stack_temp = stack.pop()
                res[stack_ind] = working_i - stack_ind

            stack.append((working_i, working_t))
        return res