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

"""
Intuition: The most difficult part of this problem is finding a way to actually represent a word
in the form of characters and the frequency of those characters. One way to do this is to create a
dictionary for each word such as {a : 1, j : 0, p : 2, ...}. Another, more effective way to do this,
is to use an array with length 26 which holds the frequency of 'a' in the 0th index, 'b' in the 1st index,
etc. The main advantage of this is that we can use this representation as a key in a dictionary after
converting it into a tuple. Also, it's really basic to update since we just have to use ord('a') - ord('c').
We do this for each of the strings and keep a tracker for the anagram groups. At the end, we just have
to return all of the values from the tracker.

Time Complexity: O(n * m)

Space Complexity: O(n)
"""