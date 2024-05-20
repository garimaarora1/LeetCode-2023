class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = defaultdict(int)
        res = ''
        mid = ''
        for n in num:
            counter[n] += 1
        sorted_numbers = sorted(list(counter.keys()))[::-1]
        for key in sorted_numbers:
            res += (counter[key]//2) * key
            counter[key] = counter[key]%2
        for key in sorted_numbers:
            if counter[key] > 0:
                mid = key
                break
        res = res + mid + res[::-1]
        res = res.strip("0")
        return res if res else "0"