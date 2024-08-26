from .. import Solution

solution = Solution()


# def test_babad():
#     assert solution.longestPalindrome("babad") == "aba"

def test_is_palindrome():
    assert solution.isPalindrome("a")
    assert solution.isPalindrome("aa")
    assert solution.isPalindrome("aba")
    assert not solution.isPalindrome("abc")
    assert solution.isPalindrome("ababa")
