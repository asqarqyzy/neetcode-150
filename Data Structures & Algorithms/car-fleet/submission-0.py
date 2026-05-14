class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)
        prev_t = None
        res = len(pairs)
        for p, s in pairs:
            t = (target - p) / s
            if prev_t is not None and t <= prev_t:
                res -= 1
            else:
                prev_t = t
        return res