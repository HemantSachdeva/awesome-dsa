class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

x = Solution()
print(x.twoSum([2, 7, 11, 15], 9))
print(x.twoSum([3, 2, 4], 6))
print(x.twoSum([3, 3], 6))
