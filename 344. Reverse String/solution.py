class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        return s


print(Solution().reverseString(["h", "e", "l", "l", "o"]))
