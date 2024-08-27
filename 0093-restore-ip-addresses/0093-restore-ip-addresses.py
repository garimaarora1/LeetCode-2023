class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        def dfs(i, parts):
            if i == n and len(parts) == 4:
                ans.append('.'.join(parts))
                return
            
            for j in range(i, n):
                # form a part
                part = s[i: j+1]
                
                if len(part) > 1 and part[0] == '0':
                    continue
                if len(part) >= 4:
                    continue
                
                if int(part) > 255:
                    continue
                parts.append(part)
                dfs(j+1, parts)
                parts.pop()
        
        dfs(0, [])
        return ans