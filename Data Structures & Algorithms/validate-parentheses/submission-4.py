class Solution:
    def isValid(self, s: str) -> bool:
        '''last opened first closed'''

        pairs = {"(": ")", "[": "]", "{": "}"}
        stack = [] 

        ''' pseudo approach'''
        if len(s) == 0 or len(s) == 1 or len(s)%2 != 0:
            return False

        for b in range(len(s)):
            if s[b] in pairs.keys():
                stack.append(s[b])
            elif s[b] in pairs.values():
                if len(stack)==0 or s[b] != pairs[stack.pop()]:
                    return False
        return len(stack) == 0
