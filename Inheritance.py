import datetime

class Player:
    def __init__(self, fname, lname, birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year


class CricketPlayer(Player):
    def __init__(self, fname, lname, birth_year, team):
        Player.__init__(self, fname, lname, birth_year)
        self.team = team
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_avg_score(self):
        return sum(self.scores)/len(self.scores)


virat = CricketPlayer('virat', 'kohli', 1988, 'India')

virat.add_score(80)
virat.add_score(110)
virat.add_score(0)
virat.add_score(90)
virat.add_score(55)

print("Age of virat kohli:", virat.get_age())
print("Average score of virat kohli:", virat.get_avg_score())

class TennisPlayer(Player):
    def __init__(self, fname, lname, birth_year, gwinner):
        Player.__init__(self, fname, lname, birth_year)
        self.grand_slam_winner = gwinner
        self.aces = []

    def get_average_aces_per_match(self):
        return sum(self.aces)/len(self.aces)

roger = TennisPlayer('roger','federer', 1981, 20)

print('Age of roger federer:',roger.get_age())