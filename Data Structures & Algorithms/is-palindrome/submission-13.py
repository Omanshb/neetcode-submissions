class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c.lower() for c in s if c.isalnum()])

        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            if s[p1] != s[p2]:
                return False

            p1 += 1
            p2 -= 1
        
        return True

"""
Intuition: The very first thing that we do is make sure that we filter our string to only include
alphanumeric characters, no spaces, and all in the same casing. Then, we initialize two pointers, one
for the left of the string and one for the right. We filter through the entire string while p1 < p2
and we keep checking that s[p1] is equal to s[p2]. Imagine the two pointers slowly converging towards
the middle. At the end, return True.

Time Complexity: O(n) since we just iterate through the string and don't look at any character multiple times.
Space Complexity: O(n) since we still just filter through the characters and that's the only manipulation being done.
"""
    