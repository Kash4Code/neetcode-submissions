class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Edge Case - If s is an empty string, then it really is a subsequence of t
        if len(s) == 0:
            return True

        i = 0 # Points to s
        j = 0 # Points to t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

            if i == len(s):
                return True
        return False
        