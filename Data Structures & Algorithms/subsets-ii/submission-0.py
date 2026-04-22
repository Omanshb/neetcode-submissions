class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        cur = []
        def helper(i):
            if i >= len(nums):
                ans.add(tuple(sorted(cur[:])))
                return
            
            cur.append(nums[i])
            helper(i + 1)
            cur.pop()
            helper(i + 1)
        helper(0)
        
        converted = [list(x) for x in ans]
        return converted