class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # O(1)
            return False
        
        sTrack = dict()
        tTrack = dict()

        for c in s: # O(n)
            sTrack[c] = sTrack.get(c, 0) + 1
        
        for c in t: # O(n)
            tTrack[c] = tTrack.get(c, 0) + 1
        
        return sTrack == tTrack # O(n)

"""
Intuition: The dictionaries for each word will contain each of the characters 
it contains and then also the count for how many times it shows up. Then, at the end
we just confirm that both of the dictionaries are equal to eachother, confirming
that the two words are valid anagrams.

Time Complexity: O(n)

Space Complexity: O(n)
"""