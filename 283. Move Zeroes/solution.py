class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
        return nums


print(Solution().moveZeroes([0, 1, 0, 3, 12]))
