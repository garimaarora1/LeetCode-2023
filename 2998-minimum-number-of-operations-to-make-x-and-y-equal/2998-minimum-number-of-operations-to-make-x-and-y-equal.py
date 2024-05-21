class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        queue = deque()
        visited = set()
        queue.append((x, 0))
        visited.add(x)
        
        while queue:
            num, step = queue.popleft()
            if num == y:
                return step
            if num % 11 == 0 and num // 11 not in visited:
                visited.add(num // 11)
                queue.append((num//11, step+1))
            if num % 5 ==0 and num //5 not in visited:
                visited.add(num // 5)
                queue.append((num//5, step+1))
            if num - 1 not in visited:
                visited.add(num-1)
                queue.append((num-1, step+1))
            if num + 1 not in visited:
                visited.add(num+1)
                queue.append((num+1, step+1))
        return -1
                