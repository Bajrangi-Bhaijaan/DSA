class Solution:
#     O(n) || O(1)
# Runtime: 54ms 64.17% memory: 13.9mb 62.75%
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandie = max(candies)
        for idx, val in enumerate(candies):
            # candies[idx] = True if not (val + extraCandies) < maxCandie else False
            candies[idx] =  not (val + extraCandies) < maxCandie
        
        return candies