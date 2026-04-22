class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {n:nums.count(n) for n in nums}

        ans = list(d.keys())
        ans.sort(key=lambda x: d[x], reverse = True)

        return ans[:k]