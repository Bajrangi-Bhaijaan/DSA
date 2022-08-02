from itertools import combinations
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        return [abs(x[0] - x[1]) for x in list(combinations(nums, 2))].count(k)