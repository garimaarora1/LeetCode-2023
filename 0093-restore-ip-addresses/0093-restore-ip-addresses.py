class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        if n < 3 or n > 12:
            return []
        
        def dfs(curr_idx, parts):
            
            if len(parts) > 4:
                return
            
            if curr_idx == n and len(parts) == 4:
                ans.append('.'.join(parts))
                return
            
            for j in range(curr_idx, min(curr_idx+3, n)):
                
                part = s[curr_idx: j+1]
                
                # skip invalid parts
                if len(part) > 1 and part[0] == '0':
                    return
                
                if int(part) > 255:
                    return
                
                parts.append(part)
                dfs(j+1, parts)
                parts.pop()
                
        
        dfs(0, [])
        
        return ans