class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        hashmap = {}

        def paint(n, color):
            if (n, color) in hashmap:
                return hashmap[(n, color)]
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                return total_cost
            elif color == 0:
                total_cost += min(paint(n + 1, 1), paint(n + 1, 2))
            elif color == 1:
                total_cost += min(paint(n + 1, 0), paint(n + 1, 2))
            elif color == 2:
                total_cost += min(paint(n + 1, 0), paint(n + 1, 1))
            hashmap[(n, color)] = total_cost
            return total_cost

        return min(paint(0, 0), paint(0, 1), paint(0, 2))
