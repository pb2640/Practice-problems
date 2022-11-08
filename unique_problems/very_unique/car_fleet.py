class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            time_taken = (target - position[i]) / speed[i]
            cars.append([position[i], speed[i], time_taken])
        cars.sort(key=lambda x: x[0])
        print(cars)
        next_t = -float("inf")
        num_fleets = 0
        for i in range(len(cars) - 1, -1, -1):
            curr_t = cars[i][2]
            if curr_t <= next_t:
                cars[i][2] = next_t
            else:
                num_fleets += 1
            next_t = cars[i][2]
        return num_fleets
