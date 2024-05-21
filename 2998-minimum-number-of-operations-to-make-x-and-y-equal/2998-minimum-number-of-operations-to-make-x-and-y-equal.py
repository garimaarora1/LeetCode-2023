class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        queue = deque()
        visited = set()
        queue.append((x,0))
        visited.add(x)
        while queue:
            ele, step = queue.popleft()
            if ele == y:
                return step
            if ele % 11 == 0 and ele//11 not in visited:
                queue.append((ele//11, step+1))
                visited.add(ele//11)
            if ele % 5 == 0 and ele//5 not in visited:
                queue.append((ele//5, step+1))
                visited.add(ele//5)
            if ele-1 not in visited:
                queue.append((ele-1, step+1))
                visited.add(ele-1)
            if ele+1 not in visited:
                queue.append((ele+1, step+1))
                visited.add(ele+1)
        return -1
            
                
            