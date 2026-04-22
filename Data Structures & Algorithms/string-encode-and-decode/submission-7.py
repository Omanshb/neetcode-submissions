class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

"""
The reason encoding is so challenging is because it's hard to use any character as a deliminator
becuase that character itself could show up in one of the strings. In this method, for every string
we add "LENGTH#STRING" to the result. Then, during decode, we read the number and # to get the
length and then from there we extract the word into it's own list item. This is fool proof since 
even if # shows up in one of the strings, we know the exact length already so we won't let this bother us.

Time complexity: O(n) just going through the list of strings once
Space complexity: O(n) just the length of the list
"""
