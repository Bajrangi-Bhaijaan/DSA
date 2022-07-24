class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ## APPROACH : GREEDY ##
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans