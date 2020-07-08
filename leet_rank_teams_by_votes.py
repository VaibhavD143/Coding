class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        rank = {c:[0]*len(votes[0])+[ord('z')-ord(c),c] for c in votes[0]}
        for vote in votes:
            for i,c in enumerate(vote):
                rank[c][i]+=1
        # y = sorted(rank.values)
        return ''.join([x[-1] for x in sorted(rank.values(),reverse=True)])