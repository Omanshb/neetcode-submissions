class MedianFinder:

    def __init__(self):
        self.h1 = []
        self.h2 = []

    def addNum(self, num: int) -> None:
        if self.h2 and num > self.h2[0]:
            heapq.heappush(self.h2, num)
        else:
            heapq.heappush(self.h1, -num)
        
        while len(self.h2) > len(self.h1) + 1:
            heapq.heappush(self.h1, -heapq.heappop(self.h2))
        
        while len(self.h1) > len(self.h2) + 1:
            heapq.heappush(self.h2, -heapq.heappop(self.h1))


    def findMedian(self) -> float:
        if len(self.h1) > len(self.h2):
            return -self.h1[0]
        elif len(self.h2) > len(self.h1):
            return self.h2[0]
        else:
            return (-self.h1[0] + self.h2[0]) / 2
        
        