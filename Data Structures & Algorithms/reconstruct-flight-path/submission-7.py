from collections import Counter

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        adj = {}
        edge_count = Counter()
        for f, t in tickets:
            adj.setdefault(f, []).append(t)
            edge_count[(f, t)] += 1

        ans = ["JFK"]

        def helper(curr):
            if len(ans) == len(tickets) + 1:
                return True
            if curr not in adj:
                return False

            for d in adj.get(curr, []):
                if edge_count[(curr, d)] > 0:
                    edge_count[(curr, d)] -= 1
                    ans.append(d)
                    if helper(d):
                        return True
                    edge_count[(curr, d)] += 1
                    ans.pop()

            return False

        helper("JFK")
        return ans