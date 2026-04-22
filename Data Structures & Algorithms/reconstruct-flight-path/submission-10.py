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

"""
Intuition: First sort the tickets so that we always take the lexigraphically right approach. Then, please
create an adjacency list to represent the graph. This is simple just like how we always do it. Then, please
set an edge count for every edge so that we can keep track of which edges have been visited so far and which
haven't. The reason we can't just use a visited set is because a single egde might show up multiple times
in our flights example. 

For the actual DFS, we will start off with a current location. Then, we will check to see if the length of
ans is equal to n + 1 yet. If so, we have used all tickets and this is a valid trip. Otherwise, we will recursively
go through each of the neighbor edges, check if that edge is valid, and then call dfs on that. We modify edge
count and the ans and then unmodify it once we return. This is a basic backtracking technique so that we can
try various different approaches. At the end, we just return the first valid True ans. 
"""