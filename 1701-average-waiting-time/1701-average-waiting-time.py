class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0
        next_idle_time = 0
        for curr_start_time, curr_prep_time in customers:
            next_idle_time = max(curr_start_time, next_idle_time) + curr_prep_time
            curr_waiting_time = next_idle_time - curr_start_time
            
            total_waiting_time += curr_waiting_time
        return total_waiting_time/len(customers)