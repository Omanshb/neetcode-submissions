class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        mx = 0
        p1, p2 = 0, 0
        while p2 < len(s):
            while s[p2] in st:
                st.remove(s[p1])
                p1 += 1
            st.add(s[p2])
            p2 += 1
            mx = max(p2 - p1, mx)
        return mx