class Solution:
    def arrayRankTransform(self, A: List[int]) -> List[int]:
        D = {j: i+1 for i,j in enumerate(sorted(set(A)))}
        return map(D.get, A)