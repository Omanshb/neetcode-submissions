class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def helper(counter, st):
            if len(st) >= n * 2:
                if counter == 0:
                    ans.append(st)
                return
        
            helper(counter + 1, st + "(")
            
            if counter > 0:
                helper(counter - 1, st + ")")
        
        helper(0, "")
        return ans