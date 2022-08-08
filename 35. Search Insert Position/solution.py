class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return end + 1


print(Solution().searchInsert([1,3,5,6], 7))
