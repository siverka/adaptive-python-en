teams = {}


def add_team(team):
    if team not in teams:
        teams[team] = {'total': 0, 'wins': 0, 'defeats': 0, 'draws': 0, 'points': 0}


def draw(team):
    teams[team]['draws'] += 1
    teams[team]['points'] += 1


def wins(team):
    teams[team]['wins'] += 1
    teams[team]['points'] += 3


def defeats(team):
    teams[team]['defeats'] += 1


def score(match):
    team1, score1, team2, score2 = match
    add_team(team1)
    add_team(team2)

    if score1 == score2:
        draw(team1)
        draw(team2)
    elif score1 < score2:
        defeats(team1)
        wins(team2)
    else:
        wins(team1)
        defeats(team2)

    teams[team1]['total'] += 1
    teams[team2]['total'] += 1


n = int(input())
for _ in range(n):
    match = input().split(sep=';')
    score(match)

for team, stat in teams.items():
    print(team, end=':')
    print(stat['total'], stat['wins'], stat['draws'], stat['defeats'], stat['points'])
