class Solution:
    def plusOne(self, digits: list) -> list:
        last_digit = digits[-1]
        if last_digit < 9:
            digits[-1] = last_digit + 1
            return digits
        elif len(digits) == 1:
            return [1, 0]
        else:
            digits[-1] = 0
            return self.plusOne(digits[:-1]) + [0]


print(Solution().plusOne([9, 9, 9]))
