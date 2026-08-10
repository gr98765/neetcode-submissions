class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        pairs = {')': '(', ']': '[', '}': '{'}

        for b in s:
            if b in pairs.values():          
                stack.append(b)
            else:                             
                if not stack or stack.pop() != pairs[b]:
                     return False
        return not stack 

