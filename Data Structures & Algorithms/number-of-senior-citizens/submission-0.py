class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for c in details:
            age = c[11:13]
            if int(age) > 60:
                count += 1
                
        return count