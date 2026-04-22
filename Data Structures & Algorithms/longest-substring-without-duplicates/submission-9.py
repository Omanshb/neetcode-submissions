class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        p = 0
        ans = 0

        for c in s:
            while c in track:
                track.remove(s[p])
                p += 1
            track.add(c)
            ans = max(ans, len(track))
        
        return ans

"""
Intuition: At any given point, you keep track of a set which holds all of the characters within the substring.
You also keep an index pointer "p", which holds the starting point of the substring. For every new character, 
if it isn't in the set, you just add it and the starting pointer doesn't change obviously. However, if the
new character is in the set already, we want to keep incrementing "p" and removing the character at that index
until we can finally add the new character without breaking our rule. At all times, for the valid substrings
keep track of the maximum length within the "ans" variable.

Time Complexity: O(n) because we just iterate over the string at most two times. Once for the index and once normally
Space Complexity: O(n) because we have to keep track of the set which makes it easy to check for our rule
"""