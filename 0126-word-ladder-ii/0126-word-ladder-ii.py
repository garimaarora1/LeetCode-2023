from collections import deque
class Solution:
    def connected(self,a,b):
        c=0
        i=0
        while i<len(a) and c<2:
            if a[i]!=b[i]:
                c+=1
            i+=1    
        return c==1

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        q=deque([beginWord]) 
        reached=False
        paths=[]
        visited=set()
        while q and not reached:
            paths.append(q.copy())
            n=len(q)
            for _ in range(n):
                word=q.popleft()
                for item in wordList:
                    if item in visited:
                        continue
                    if not self.connected(word,item):
                        continue
                    if item== endWord:
                        reached=True
                        break   
                    q.append(item)
                    visited.add(item)
                if reached:
                    break
        if not reached:
            return []

        ans=[]

        def backtrack(word,level,steps):
            if word==beginWord:
                ans.append(steps[::-1])
                return
            if level<0:
                return
            for item in paths[level]:
                if not self.connected(word,item):
                    continue
                steps.append(item)
                backtrack(item,level-1,steps)
                steps.pop()        
            
        backtrack(endWord,len(paths)-1,[endWord])  
        return ans     





        