class Solution:
    
    def rankTeams(self, votes: List[str]) -> str:
        def func(second, first):
            second_array = d[second]
            first_array = d[first]
            if second_array > first_array:
                return -1
            return 1
        l = len(votes[0])
        d = {ch: [0]*l for ch in votes[0]}
        for vote in votes:
            for i, char in enumerate(vote):
                d[char][i] += 1
        sorted_keys = sorted(list(d.keys()))
        sorted_keys.sort(key=cmp_to_key(func))
        return ''.join(sorted_keys)
        
        
            