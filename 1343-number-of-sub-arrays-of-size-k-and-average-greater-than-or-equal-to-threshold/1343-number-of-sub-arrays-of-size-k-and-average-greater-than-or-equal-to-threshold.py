class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = 0 
        j = 0
        counter = 0
        for i in range(len(arr)):
            window_sum += arr[i]
            if i-j+1 == k:
                avg = window_sum / k
                if avg >= threshold:
                    counter += 1
                window_sum -= arr[j]
                j += 1
        return counter
                