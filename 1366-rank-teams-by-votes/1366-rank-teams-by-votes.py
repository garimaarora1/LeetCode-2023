class Solution:
    
    def rankTeams(self, votes: List[str]) -> str:
        def func(x):
            return 
        d = {ch: [0] * len(votes[0]) for ch in votes[0]} 
        res = ''
        for vote in votes:
            for rank, ch in enumerate(vote):
                d[ch][rank] += 1
        sorted_keys = sorted(d.keys())
        return "".join(sorted(sorted_keys, key=lambda x: d[x], reverse=True))
            