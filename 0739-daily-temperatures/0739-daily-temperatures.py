class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ms = []
        ans = []
        for i in range(len(temperatures)-1, -1, -1):
            while ms and ms[-1][0] <= temperatures[i]:
                ms.pop()
            if ms:
                ans.append(ms[-1][1]-i)
            else:
                ans.append(0)
            ms.append((temperatures[i], i))
        return ans[::-1]
        