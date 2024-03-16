import datetime
class CricketPlayer:
    def __init__(self, fname, lname, team, birth_year):
        self.first_name =fname
        self.last_name = lname
        self.team = team
        self.birth_year = birth_year
        self.scores = []

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def add_score(self, score):
        self.scores.append(score)

    def get_avg_score(self):
        return sum(self.scores)/len(self.scores)

    def __lt__(self, other):
        my_score = self.get_avg_score()
        other_score = other.get_avg_score()
        return my_score < other_score

    def __str__(self):
        return f'{self.first_name} {self.last_name} the cricket player from {self.team} '


virat = CricketPlayer('virat','kohli', 'India', 1988)

virat.add_score(80)
virat.add_score(110)
virat.add_score(0)
virat.add_score(90)
virat.add_score(55)

print(virat)

print(f'virat average score = {virat.get_avg_score()}')

david = CricketPlayer('david','warner', 'australia', 1986)

david.add_score(60)
david.add_score(90)
david.add_score(110)
david.add_score(0)
david.add_score(65)

print(david)

print(f'david average score = {david.get_avg_score()}')

print(virat < david)