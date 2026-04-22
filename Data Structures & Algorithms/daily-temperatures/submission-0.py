class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stck = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stck and temperatures[i] > temperatures[stck[-1]]:
                print(i, stck[-1])
                answer[stck[-1]] = i - stck[-1]
                stck.pop()
            
            stck.append(i)
        
        return answer