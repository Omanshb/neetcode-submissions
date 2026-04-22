class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker = [0] * 26
        p = 0
        ans = 0
        mx = 0

        for i in range(len(s)):
            tracker[ord(s[i]) - ord('A')] += 1
            mx = max(mx, tracker[ord(s[i]) - ord('A')])

            while mx + k < i - p + 1:
                tracker[ord(s[p]) - ord('A')] -= 1
                p += 1
            
            ans = max(ans, i - p + 1)
        
        return ans

"""
Intuition: First of all, let's figure out what the process is for figuring out if a specific window is valid
or not. In this case, the way we do this is by taking the count of the letter that shows up the most and then
adding k to this value. If this value is still less than i - p + 1 (length of the interval), that means the 
window is not valid. In this case, we keep removing from the start of the interval until it's finally valid.
One of the most difficult aspects of this problem is keeping track of the maximum letter during the calculations.
To do this, we just keep an ordinal array of all the letters a-z and, when we're updating their counts, we just 
also figure out the max at that specific point. Throughout this whole process, keep track of the ans as a max holder.

Time Complextiy: O(n) since we just iterate over the list and update/remove at each step. You could also say 26 * n
since we are calculating the max at every step.

Space Complexity: O(1) since we're just holding variables like p, ans, mx, and the tracker (26-length array). None
of these are dependent on the size of the array so the space complexity is still O(1) technically).
"""
