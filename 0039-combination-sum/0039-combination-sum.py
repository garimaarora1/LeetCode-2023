class Solution:
    """
    - Use Depth-First Search (DFS) to explore all possible combinations.
    - For each recursive call, consider only the current index and onwards to avoid         permutations of the same combination.
    - Ensure each number can be used multiple times but avoid revisiting previous           indices to avoid duplicate combinations.
    Time Complexity: O(N^((T/M)+1)) 
    Space Complexity: O(N^(T/M)
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
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
        
        dfs(0, [], 0)
        return ans