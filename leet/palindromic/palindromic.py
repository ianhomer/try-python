class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        best = s[0]
        for i in range(len(s)):
            for j in range(length - i):
                candidate = s[i : i + j + 1]
                if self.isPalindrome(candidate) and len(candidate) > len(best):
                    best = candidate
        print(best)
        return best

    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        mid = int(len(s) / 2)
        return s[:mid] == s[::-1][:mid]
