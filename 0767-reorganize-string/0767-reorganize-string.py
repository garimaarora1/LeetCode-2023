class Solution:
    def reorganizeString(self, s: str) -> str:
        # counter 
        # max heap (-ve values )
        # heapfiy 
        # prev, res
        # while prev heap 
        # prev not heap : return res
        # cnt, char 
        # cnt + 1, add char to res 
        # if prev: push to heap
        # ic cnt !=0 set prev
        # return res
        counter = Counter(s)
        # max heap
        heap = [(-cnt, char) for char, cnt in counter.items()]
        heapq.heapify(heap)
        prev = None
        res = ''
        while heap or prev:
            if prev and not heap:
                # important
                return ""
            cnt, char = heapq.heappop(heap)
            res += char
            cnt += 1 
            if prev:
                heapq.heappush(heap, prev)
                 # important
                prev = None
            if cnt != 0:
                prev = (cnt, char)
        return res