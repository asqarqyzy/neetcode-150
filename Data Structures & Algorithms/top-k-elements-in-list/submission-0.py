class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {}
        result = []
        for num in nums:
            dict_nums[num] = dict_nums.get(num, 0) + 1

        freq_arr = [[] for i in range(len(nums) + 1)]

        for k, v in dict_nums.items():
            freq_arr[v].append(k)

        for i in range(len(freq_arr) - 1, 0, -1):
            for num in freq_arr[i]:
                result.append(num)
                if len(result) == k:
                    return result
