class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        for i, target in enumerate(words):
            for j, other in enumerate(words):
                if target in other and i != j:
                    result.add(target)
        return list(result)