class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = [[False] * len(heights[x]) for x in range(len(heights))]
        atlantic = [[False] * len(heights[x]) for x in range(len(heights))]
        pac = True

        def helper(x, y, prev):
            nonlocal pac

            if x not in range(len(heights)) or y not in range(len(heights[0])) or heights[x][y] < prev:
                return
            
            if pac:
                if pacific[x][y]:
                    return
                pacific[x][y] = True
            else:
                if atlantic[x][y]:
                    return
                atlantic[x][y] = True
            
            helper(x + 1, y, heights[x][y])
            helper(x - 1, y, heights[x][y])
            helper(x, y + 1, heights[x][y])
            helper(x, y - 1, heights[x][y])

        for i in range(len(heights[0])):
            pac = True
            helper(0, i, -float('inf'))

            pac = False
            helper(len(heights) - 1, i, -float('inf'))
        
        for i in range(len(heights)):
            pac = True
            helper(i, 0, -float('inf'))
            
            pac = False
            helper(i, len(heights[0]) - 1, -float('inf'))
        
        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        return ans

"""
Intuition: Instead of trying to check every single node to see if it reaches both of the oceans,
we reverse the problem on it's head. We start off with every single pacific ocean and atlantic ocean
point and then traverse up. As we're doing this, we flag every square one as True for that specific
ocean. Then, at the end, we just append all of those squares which have True for both of the oceans
to the answer list and return that. Flipping the question on it's head is way easier than trying to
calculate if each square has the ability to end up on either pacific or atlantic.
"""
