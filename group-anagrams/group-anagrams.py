# strs = ["eat","tea","tan","ate","nat","bat"]
#           i
#
#
# anagram = {} {}
# counter = 0
# [["eat", "tea"], ["tan"]]

# Time complexity: O(n + nlogn) = O(nlogn) where n = size list and nlogn is from sort function
# Space complexity: O(n + m) = O(n) and m is the size of my new list n is the size of my dictionary

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        counter = 0
        anagram = {}
        for s in strs:
            sorts = "".join(sorted(s))
            if sorts in anagram:
                ans[anagram[sorts]].append(s)
            else:
                newList = []
                newList.append(s)
                ans.append(newList)
                anagram[sorts] = counter
                counter += 1
                
        return ans
            