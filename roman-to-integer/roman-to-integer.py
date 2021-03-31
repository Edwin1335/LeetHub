class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
        out = 0
        i = len(s)-1
        
        while i >= 0:
            if i == 0:
                out += rom[s[i]]
                break
            if rom[s[i-1]] >= rom[s[i]]:
                out += rom[s[i]]
                i -= 1
            else:
                out += (rom[s[i]] - rom[s[i-1]])
                i -= 2
            
        return out

            