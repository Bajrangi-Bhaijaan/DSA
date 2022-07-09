class Solution:
    def countPoints(self, rings: str) -> int:
        rods=[set() for _ in range(10)]
        n=len(rings)
        for i in range(0,n,2):
            color=rings[i]
            rod=int(rings[i+1])
            rods[rod].add(color)
        return sum(len(s)==3 for s in rods)    