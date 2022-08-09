class Solution:
    def sortedSquares(self, nums: list) -> list:
        return sorted([x**2 for x in nums])
