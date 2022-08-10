class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[-i - 1]
            s[-i - 1] = temp
        return s


print(Solution().reverseString(["h", "e", "l", "l", "o"]))
