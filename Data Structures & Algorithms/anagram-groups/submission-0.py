class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anag = {}
        
        for s in strs:
            key = "".join(sorted(s))

            if key in dict_anag:
                dict_anag[key].append(s)
            else:
                dict_anag[key] = [s]
        
        return list(dict_anag.values())