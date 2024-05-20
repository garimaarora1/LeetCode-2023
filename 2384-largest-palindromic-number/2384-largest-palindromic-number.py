class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = defaultdict(int)
        res = ''
        mid = 0
        for n in num:
            counter[n] += 1
        sorted_numbers = sorted(list(counter.keys()))
        sorted_numbers = sorted_numbers[::-1]
        for key in sorted_numbers:
            if counter[key]%2 == 0:
                res += (counter[key]//2) * key
                counter[key] = 0
            elif counter[key]-1>0:
                res += (counter[key]//2) * key
                counter[key] = 1
        for key in sorted_numbers:
            if counter[key] > 0:
                mid = key
                break
        if mid:
            res = res + mid + res[::-1]
        else:
            res = res + res[::-1]
        res = res.strip("0")
        return res if res else "0"