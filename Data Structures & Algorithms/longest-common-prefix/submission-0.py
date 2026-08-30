class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first_word = strs[0]
        for i in range(len(first_word)):
            char_to_match = first_word[i]
            for word in strs[1:]:
                if i == len(word) or word[i] != char_to_match:
                    return first_word[:i]
        return first_word

        