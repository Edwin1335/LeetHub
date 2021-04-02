from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        length = len(s1)
        count = Counter(s1)
        for i in range(len(s2)):
            count2 = Counter(s2[i:length+i])
            if count2 == count:
                return True
        return False
