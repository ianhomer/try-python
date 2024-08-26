class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        best = s[0]
        bestLength = 1
        for i in range(len(s)):
            for j in range(length - i - bestLength):
                if s[i] != s[length - j - 1]:
                    pass
                if length - j - i > bestLength and self.isPalindrome(s, i, -j):
                    best = s[i : length - j]
                    bestLength = len(best)
        return best

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
