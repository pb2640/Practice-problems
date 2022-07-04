# 1366. Rank Teams by Votes
# Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
# Output: "ACB"
"""
Idea, for ever vote in votes. Add the team in a hashmap and record no. of votes it got for each position
then sort the poistions alphabetically and then by the votes and join to get the final string.
"""


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        ref = {}
        for vote in votes:
            for i in range(len(vote)):
                if vote[i] in ref:
                    ref[vote[i]][i] += 1
                else:
                    ref[vote[i]] = [0] * len(vote)
                    ref[vote[i]][i] = 1

        ans = sorted(ref.keys())

        return "".join(sorted(ans, key=lambda x: ref[x], reverse=True))
