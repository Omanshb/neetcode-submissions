class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            n = ''.join(sorted(s))
            mp[n] = mp.get(n, []) + [s]
        
        return [mp[i] for i in mp]