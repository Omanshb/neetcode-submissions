class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            print(string)
            key = tuple(sorted(string))
            groups[key] = groups.get(key, []) + [string]
        
        return list(groups.values())