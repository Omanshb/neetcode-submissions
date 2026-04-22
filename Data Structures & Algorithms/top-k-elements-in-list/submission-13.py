class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {n:nums.count(n) for n in nums}

        
        freq = [[] for x in range(len(nums))]


        for key, value in tracker.items():
            freq[value - 1].append(key)
        
        ans = []
        for i in range(len(freq) - 1, -1, -1):
            ans += freq[i]
            if len(ans) >= k:
                break

        return ans[:k]

"""
Intuition: There is a naive way to do this which just involves holding a dictionary of the numbers
and their frequency. Then, sorting the keys of the dictionary by using a custom lambda function and
returning the top k. However, the more efficient way to do this is using frequency buckets. You create
a frequency array of length n. If a number is in freq[i], it means that it has shown up i times. Once
you create a dictionary with the num counts, instead of sorting, populate this frequency array and then 
iterate through it backwards k total times.

Time Complexity: O(n)

Space Complexity: O(n)
"""