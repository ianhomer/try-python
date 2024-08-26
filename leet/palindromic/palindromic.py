class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        best = s[0]
        bestLength = 1
        for i in range(len(s)):
            for j in range(length - i - bestLength):
                candidate = s[i : length - j]
                if len(candidate) > bestLength and self.isPalindrome(candidate):
                    best = candidate
                    bestLength = len(best)
        return best

    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        mid = int(len(s) / 2)
        return s[:mid] == s[::-1][:mid]
