class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1:
            n = sum([int(i)**2 for i in str(n)])

            if n in visited:
                return False
            else:
                visited.add(n)
        return True


print(Solution().isHappy(19))
print(Solution().isHappy(2))
