class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key = lambda x: x[0], reverse=True)
        destination_time = [(target - cars[i][0]) / cars[i][1] for i in range(len(cars))]

        stck = []
        for t in destination_time:
            if stck and t <= stck[-1]:
                continue
            stck.append(t)

        return len(stck)