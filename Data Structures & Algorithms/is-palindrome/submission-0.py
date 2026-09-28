class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        1) initialize start and end 
        2) keep iterating till you hit a middle 
        3) if at any point the mirrored points do not match return false
        4) return true at the end 
        '''

        start = 0
        end = len(s)-1

        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        
        return True
