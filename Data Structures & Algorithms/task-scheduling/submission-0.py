class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        count.sort()
        maxf = count[25]

        # Calculate the number of total idle spots
        idle = (maxf - 1) * n

        for i in range(24, -1, -1):
            # for each unique task type, subtract the appropriate number of idle spots
            idle -= min(maxf - 1, count[i])
        
        # the answer is just the total number of idle spots we have + the number of tasks
        return max(0, idle) + len(tasks)