class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for st in strs:
            new = ''.join(sorted(st))
            print(new, st)
            groups[new] = groups.get(new, []) + [st]
        
        return list(groups.values())