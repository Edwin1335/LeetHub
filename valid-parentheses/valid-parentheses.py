class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        
        for x in s:
            if x in "({[":
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == self.partnerParen(x):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
    
    def partnerParen(self, char):
        if char == ')':
            return '('
        elif char == '}':
            return '{'
        else:
            return '['
                