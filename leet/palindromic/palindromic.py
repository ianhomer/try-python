class Solution:
    def longestPalindrome(self, s: str) -> str:
        return s

    def isPalindrome(self, s: str) -> bool:
        if (len(s) < 2):
            return True
        mid = int(len(s) / 2)
        return s[:mid] == s[::-1][:mid]
