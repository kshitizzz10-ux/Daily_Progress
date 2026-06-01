class Innings:
    
    MAX_WICKETS = 10
    def __init__(self,batting_team,bowling_team):
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self._run_scored = 0
        self._legal_deliveries = 0
        self._wickets = 0
        self._extras = 0
    def add_runs(self, runs_scored):
        self._run_scored += runs_scored
    def add_wicket(self):
        self._wickets += 1
    def add_legal_delivery(self):
        self._legal_deliveries += 1
    def current_run_rate(self):
        if self._legal_deliveries != 0 :
            return self._run_scored /(self._legal_deliveries/6)
        else:
            return 0.0    
    @classmethod
    def from_string(cls, match_string):

        batting_team , bowling_team = match_string.split('-')
        return cls(batting_team, bowling_team)
    
class ODIInnings(Innings):
    MAX_OVERS = 50
class T20Innings(Innings):
    MAX_OVERS = 20

    
match_A = Innings(batting_team="India",bowling_team="Australia")
match_B = Innings(batting_team="RCB",bowling_team="RR")
match_A.add_runs(6)
match_A.add_legal_delivery()
match_A.add_wicket()
match_1 = T20Innings.from_string("INDIA-AUSTRALIA")
match_2 = ODIInnings.from_string("INDIA-ENGLAND")
print(match_1.MAX_OVERS)
print(match_2.MAX_OVERS)
match_1.add_runs(6)
match_2.add_runs(4)
print(f"SCORE: {match_1._run_scored} / {match_1._wickets}")
print(f"SCORE: {match_2._run_scored} / {match_2._wickets}")

print(f"India's scorecard is {match_A._run_scored}/{match_A._wickets} , RR : {match_A.current_run_rate()}")