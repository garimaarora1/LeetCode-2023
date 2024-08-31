class Solution:
    def feasible(self, weights: List[int], capacity: int, days: int) -> bool:
        days_needed = 1
        current_load = 0
        for weight in weights:
            current_load += weight
            if current_load > capacity:
                days_needed += 1
                current_load = weight
                if days_needed > days:
                    return False
        return True
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_load = sum(weights)   # high
        max_load = max(weights)    # low 

        left, right = max_load, total_load
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if self.feasible(weights, mid, days):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
