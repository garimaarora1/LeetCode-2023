class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited=set()
        q=deque()
        q.append("")
        n=len(s)
        while q:
            sub=q.popleft()
            if sub==s:
                return True
            if len(sub)>=len(s):
                continue
            for word in wordDict:
                newword=sub+word
                l=len(newword)
                if len(newword)<=len(s) and newword not in visited and newword==s[:l]:
                    q.append(newword)
                    visited.add(newword)
        return False            
                    