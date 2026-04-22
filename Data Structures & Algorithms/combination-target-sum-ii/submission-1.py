class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []

        def helper(sm, i):
            if sm > target:
                return
            
            if i >= len(candidates):
                if sm == target:
                    ans.append(curr.copy())
                return 
            
            curr.append(candidates[i])
            helper(sm + candidates[i], i + 1)
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            helper(sm, i + 1)

        candidates.sort()
        helper(0, 0)

        return ans