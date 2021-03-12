class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
    
        for x in s:
            if x.isalnum():
                new_string += x.lower()
                
        left, right = 0, len(new_string)-1
        while left < right:
            if new_string[left] != new_string[right]:
                return False
            left += 1
            right -= 1
            
        return True