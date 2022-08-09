class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums.pop())
        return nums


print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 2))
