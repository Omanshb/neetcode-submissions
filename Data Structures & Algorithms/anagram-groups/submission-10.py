class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}

        for s in strs:
            alpha = [0] * 26
            for c in s:
                alpha[ord('a') - ord(c)] += 1
            alpha = tuple(alpha)

            tracker[alpha] = tracker.get(alpha, []) + [s]
        
        return [lst for lst in tracker.values()]