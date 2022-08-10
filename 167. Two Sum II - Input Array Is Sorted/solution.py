class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        start, end = 0, len(numbers) - 1
        
        while start != end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start + 1, end + 1]


print(Solution().twoSum([2,3,4], 6))
