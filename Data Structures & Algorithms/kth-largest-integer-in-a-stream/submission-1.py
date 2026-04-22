import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = [-n for n in nums]
        heapq.heapify(self.pq)

    def add(self, val: int) -> int:
        print(self.pq)
        heapq.heappush(self.pq, -val)
        lst = []
        for i in range(self.k - 1):
            lst.append(heapq.heappop(self.pq))
        ans = -heapq.heappop(self.pq)
        heapq.heappush(self.pq, -ans)
        for n in lst:
            heapq.heappush(self.pq, n)
        
        return ans
