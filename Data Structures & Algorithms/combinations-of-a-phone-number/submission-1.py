class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []

        letters = {
        "2":["a", "b", "c"],
        "3":["d", "e", "f"],
        "4":["g", "h", "i"],
        "5":["j", "k", "l"],
        "6":["m", "n", "o"],
        "7":["p", "q", "r", "s"],
        "8":["t", "u", "v"],
        "9":["w", "x", "y", "z"]
        }

        def helper(s, i):
            # end when i exceeds our digits length
            if i >= len(digits):
                if s:
                    ans.append(s)
                return
            
            # add every possible digit
            for l in letters[digits[i]]:
                helper(s + l, i + 1)
        
        helper("", 0)

        return ans