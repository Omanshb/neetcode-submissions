class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {n:nums.count(n) for n in nums}

        
        sorted_nums = list(tracker.keys())
        sorted_nums.sort(key=lambda x: tracker[x], reverse=True)

        return sorted_nums[:k]