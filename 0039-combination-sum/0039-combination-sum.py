class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(i, subset,current_sum):
            # base condition
            if current_sum == target:
                res.append(subset[:])
                return
            if i == len(candidates):
                return 
            for j in range(i,len(candidates)):
                if current_sum + candidates[j] > target:
                    continue
                subset.append(candidates[j])
                # choose as many timesss
                backtrack(j, subset, current_sum + candidates[j])
                subset.pop()  
                
        res=[]
        backtrack(0, [], 0)
        return res