class Solution:
    """
    Find all unique combinations in `candidates` where the candidate numbers sum up       to `target`.
    Each number in `candidates` can be used an unlimited number of times.
    Time Complexity: O(2^N) where N is the length of `candidates`
    Space Complexity: O(N) where N is the length of the current combination
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr_ans = []
        n = len(candidates)
        
        def dfs(i, curr_ans, curr_sum):
            if curr_sum > target:
                return
            if curr_sum == target:
                ans.append(curr_ans.copy())
                return
            
            for j in range(i, n):
                curr_ans.append(candidates[j])
                curr_sum += candidates[j]
                dfs(j, curr_ans, curr_sum)
                curr_sum -= curr_ans.pop()
        
        dfs(0, curr_ans, 0)
        return ans