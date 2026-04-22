import heapq
class MedianFinder:
    def __init__(self):
        self.pq = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.pq, num)

    def findMedian(self) -> float:
        ln = len(self.pq)
        removed = []
        median = 0
        for i in range(ln // 2):
            removed.append(heapq.heappop(self.pq))
        if ln % 2 == 1:
            removed.append(heapq.heappop(self.pq))
            median = removed[-1]
        else:
            removed.append(heapq.heappop(self.pq))
            median = (removed[-1] + removed[-2]) / 2
        while removed:
            heapq.heappush(self.pq, removed.pop())
        return median
        