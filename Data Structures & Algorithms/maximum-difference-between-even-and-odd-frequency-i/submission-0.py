class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0] * 26

        for char in s:
            freq[ord(char) - ord('a')] += 1

        max_odd = 0
        min_even = float('inf')

        for f in freq:
            if f > 0:
                if f % 2 != 0:
                    max_odd = max(max_odd, f)
                else:
                    min_even = min(min_even, f)
                
        return max_odd - min_even