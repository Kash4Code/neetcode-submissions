class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if len(t) == 0:
            return 0

        i = 0  # pointer for s
        j = 0  # pointer for t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
            
            
        return len(t) - j
        

        
