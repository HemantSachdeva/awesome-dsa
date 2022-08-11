class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = list()
        for word in words:
            chars = list(word)
            start = 0
            end = len(chars) - 1
            while start < end:
                temp = chars[start]
                chars[start] = chars[end]
                chars[end] = temp
                start += 1
                end -= 1
            reversed_word = ''.join(chars)
            reversed_words.append(reversed_word)
        return ' '.join(reversed_words)


print(Solution().reverseWords("Let's take LeetCode contest"))
