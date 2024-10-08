class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # GSWEP problem

        # approach:

        # hashmap team : index
        # init teamList = [((numVotesAtFirstPlace, ...numVotesAtNPlace, teamName), ...]
        # 2d map of [team][place] -> voteNum

        # init result string
        # sort teamList.sort(reverse=True)
        # "".join(teamList[-1])

        # keep an iterable of teams and votes = intermediate_list = [(2,2,1, 'teamA'), (3,3,2, 'teamB')]
        # compare the teams to build the result string
        # pop off the team that makes it to that place

        # Time: O(v * n), Space: O(n) where n is the amount of teams

        # My solution
        num_of_teams = len(votes[0])
        team_to_vote_index = {}
        team_list = []
        
        # build data structures
        for team_name in votes[0]:
            if team_name not in team_to_vote_index:
                team_to_vote_index[team_name] = len(team_list)
                
            team_list.append([ [0 for x in range(num_of_teams)], team_name ] )
            
        # count votes
        for vote in votes:
            for i in range(len(vote)):
                team_name = vote[i]
                index_for_team = team_to_vote_index[team_name]
                
                team_list[index_for_team][0][i] -= 1
                
        team_list.sort()
        
        result = ""
        for team in team_list:
            result += team[1]
        
        return result

        # Fred's solution
        # def get_counts(votes):
        #     places = len(votes[0])
        #     teams = set(votes[0])

        #     team_counters = defaultdict(lambda: defaultdict(int))
        #     for vote in votes:
        #         for place in range(len(vote)):
        #             team = vote[place]
        #             team_counters[team][place] -= 1
        #     return team_counters

        # def convert_tuple(team_dict, places):
        #     result = []
        #     for place in range(places):
        #         result.append(team_dict[place])
        #     return tuple(result)

        # counts = get_counts(votes)
       
        # sorted_teams = []
        # for team in counts.keys():

        #     sorted_teams.append((convert_tuple(counts[team], len(votes[0])), team))
        #     sorted_teams.sort()
        
        # return "".join([team for _,team in sorted_teams])
