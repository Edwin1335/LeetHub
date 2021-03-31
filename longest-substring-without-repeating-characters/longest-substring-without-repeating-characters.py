#   a   b   b   a
#           l   
#               i
#
#   seen = {'a': 0, 'b':1, }
#   longest = 3
#   

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        lenght = len(s)
        longest = 0
        seen = {}
        
        for index, char in enumerate(s):
            if char in seen and left <= seen[char]:
                left = seen[char] + 1
            seen[char] = index
            longest = max(longest, (index - left + 1))
            # print("Left ",left, "Right ", index, longest)

        return longest
            
                