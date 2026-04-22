class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in intervals[1:]:
            if i[0] > res[-1][1]:
                res.append(i)
            else:
                prev = res.pop()
                res.append([min(prev[0], i[0]), max(prev[1], i[1])])
        return res
            
