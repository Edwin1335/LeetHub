#
#   "t m m z u x t"
#                i
#        S


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        repChar = {}

        for i in range(len(s)):
            if s[i] in repChar and start <= repChar[s[i]]:
                start = repChar[s[i]] + 1
            else:
                longest = max(longest, i - start + 1)
            repChar[s[i]] = i

        return longest