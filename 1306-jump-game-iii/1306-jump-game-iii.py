class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = deque([start])

        while q:
            node = q.popleft()
            # check if reach zero
            if arr[node] == 0:
                return True
            if arr[node] < 0:
                continue

            # check available next steps
            for i in [node + arr[node], node - arr[node]]:
                if 0 <= i < n:
                    q.append(i)

            # mark as visited
            arr[node] = -arr[node]

        return False