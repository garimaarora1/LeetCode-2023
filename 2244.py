from collections import defaultdict
import math
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ans = 0
        d = defaultdict(int)
        for i in range(len(tasks)):
            d[tasks[i]] += 1
        for i in d.values():
            if i == 1:
                return -1
            ans += math.ceil(i/3)
        return ans
            
            

        
        
