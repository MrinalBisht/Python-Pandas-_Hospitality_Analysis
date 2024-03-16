import datetime

virat = {
    'first_name' : 'virat',
    'last_name' : 'kohli',
    'birth_year' : 1988,
    'scores': []
}

virat['scores'].append(80)
virat['scores'].append(0)
virat['scores'].append(120)
virat['scores'].append(70)
virat['scores'].append(85)

def get_age(player):
    now = datetime.datetime.now()
    return now.year -player['birth_year']

def get_avg_score(player):
     return sum(player["scores"])/len(player["scores"])


david = {
    'first_name' : 'david',
    'last_name' : 'warner',
    'birth_year' : 1986,
    'scores': []
}

david['scores'].append(90)
david['scores'].append(0)
david['scores'].append(100)
david['scores'].append(80)
david['scores'].append(75)

print(get_age(david))
print(get_avg_score(david))