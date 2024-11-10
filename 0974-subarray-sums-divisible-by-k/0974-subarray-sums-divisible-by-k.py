class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # curr_reminder: freq
        mod_dict = defaultdict(int)
        mod_dict[0] = 1
        curr_sum = 0
        curr_reminder = 0
        count = 0
        
        for num in nums:
            curr_sum += num
            curr_reminder = curr_sum % k
            if curr_reminder < 0:
                curr_reminder += k
            count += mod_dict[curr_reminder]
            mod_dict[curr_reminder] += 1

        return count