class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0
        next_start_time = 0
        curr_waiting_time = 0
        for curr_start_time, curr_prep_time in customers:
            
            if next_start_time > curr_start_time:
                curr_waiting_time = next_start_time - curr_start_time
                next_start_time += curr_prep_time
            else:
                next_start_time = curr_start_time + curr_prep_time 
                curr_waiting_time = 0
            curr_waiting_time += curr_prep_time
            
            total_waiting_time += curr_waiting_time
        return total_waiting_time/len(customers)