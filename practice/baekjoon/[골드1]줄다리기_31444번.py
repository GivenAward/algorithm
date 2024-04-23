# [1, 2], [3] -> 87
# [1, 3], [2] -> 36
# [2, 3], [1] -> 91
# max([87, 36, 91]) -> 91

# [1, 2], [3, 4] -> 1, 4 -> 1
# [1, 3], [2, 4] -> 2, 1 -> 1
# [1, 4], [2, 3] -> 3, 2 -> 2
# [1], [2, 3, 4] -> 2, 1, 4 -> 1
# [2], [1, 3, 4] -> 2, 3, 4 -> 2
# [3], [1, 2, 4] -> 1, 3, 1 -> 1
# [4], [1, 2, 3] -> 1, 2, 2 -> 1
# max([1, 1, 2, 1, 2, 1, 1]) -> 2
import sys


def find_min_value(graph, team1, team2):
    min_value_team1 = 10**6 + 1
    min_value_team2 = 10**6 + 1

    for i in team1:
        for j in team1:
            if i != j and graph[i - 1][j - 1] != 0:
                min_value_team1 = min(min_value_team1, graph[i - 1][j - 1])

    for i in team2:
        for j in team2:
            if i != j and graph[i - 1][j - 1] != 0:
                min_value_team2 = min(min_value_team2, graph[i - 1][j - 1])

    return min(min_value_team1, min_value_team2)


def find_teamwork(n, graph):
    n = list(range(1, n + 1))

    def division_two_teams(n, graph, team1, team2, made_team, index):
        global result
        if index == len(n):
            if len(team1) > 0 and len(team2) > 0:
                made_team.append(team1)
                made_team.append(team2)
                result = max(find_min_value(graph, team1, team2), result)
            return

        if team1 + [n[index]] in made_team:
            return
        if team2 + [n[index]] in made_team:
            return
        division_two_teams(n, graph, team1 + [n[index]], team2, made_team, index + 1)
        division_two_teams(n, graph, team1, team2 + [n[index]], made_team, index + 1)

    division_two_teams(n, graph, [], [], [], 0)
    print(result)


input_ = sys.stdin.readline
n = int(input_())
graph = [list(map(int, input_().split())) for _ in range(n)]
result = 0
find_teamwork(n, graph)

"""
Input1
3
0 87 36
87 0 91
36 91 0

Output1
91

Input2
4
0 1 2 3
1 0 2 1
2 2 0 4
3 1 4 0

Output2
2
"""
