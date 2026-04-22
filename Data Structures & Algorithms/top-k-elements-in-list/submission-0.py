class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in counts[:k]]