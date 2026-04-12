class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        bottoms = []
        while r < len(height) - 1:
            if height[l] == 0:
                l += 1
                r += 1
            if height[r] < height[l]:
                bottoms.append(height[r])
                r += 1
            if height[r] >= height[l]:
                cur_res = 0
                for base in bottoms:
                    cur_res += min(height[l], height[r]) - base
                bottoms = []
                res += cur_res
                l = r
                r += 1
        return res
