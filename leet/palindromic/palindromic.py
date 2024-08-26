class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        result = ""

        def findPalindrome(left, right):
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1: right]

        for i in range(length):
            result = max(result, findPalindrome(i, i), findPalindrome(i, i+1), key=len)
        return result

    def isPalindrome(self, s: str, start=0, end=0) -> bool:
        assert end < 1  # end must be a negative value to indicate distance from end
        length = len(s) + end - start
        if length < 2:
            return True
        mid = int(length / 2)
        for i in range(mid):
            if s[start + i] != s[-1 - i + end]:
                return False
        return True
