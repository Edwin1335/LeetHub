#    0  1   2   3   4
#   "b"
#    X   
#    l 
#    r      
#   
#   out_pali = [a   b   b   a]
#   index_pali = []
#
#
#   "b"     "bab"
#   "bb"    "baab"
#   
#   
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            index_palindrome1 = self.helper(s, i, i)
            index_palindrome2 = self.helper(s, i, i+1)
            if len(index_palindrome1) > len(index_palindrome2) and len(index_palindrome1) > len(answer):
                answer = "".join(index_palindrome1)
            elif len(index_palindrome2) > len(index_palindrome1) and len(index_palindrome2) > len(answer):
                answer = "".join(index_palindrome2)
        return answer
    def helper(self, s, l, r):
        index_palindrome = []
        while l >= 0 and r < len(s) and s[l] == s[r]:
            index_palindrome = s[l: r+1]
            l -= 1
            r += 1
        return index_palindrome