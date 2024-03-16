# f = open('C:\\Users\crypt\OneDrive\Desktop\\funny.txt', 'r')
#
# for line in f:
#     print(line)
#
# f.close()
#
# with open('C:\\Users\crypt\OneDrive\Desktop\\funny.txt', 'r') as f:
#     for line in f:
#         print(line)                # with statement we don't need to close file
#
# with open('C:\\Users\crypt\OneDrive\Desktop\\funny.txt', 'r') as f:
#     lines = f.readlines()
#     print(lines)
#
# with open('Sarcasm.txt', 'a') as f:
#     f.write("\nIf words can kill you, you better ignore them ") # a represents append so it adds to lines
#
# with open('Sarcasm.txt', 'w') as f:
#     f.writelines([
#         "I love java",
#         "\nI love C++",
#         "\nBut my true love is pyhton"
#     ])
#
# with open("C:\\Users\crypt\OneDrive\Desktop\\scores.csv", "r") as f:
#     for line in f:
#         player, score = line.split(',')
#         score = int(score)
#         print(player, score)
#
# player_scores = {}
#
# with open("C:\\Users\crypt\OneDrive\Desktop\\scores.csv", "r") as f:
#     for line in f:
#         player, score = line.split(',')
#         score = int(score)
#         if player in player_scores:
#             player_scores[player].append(score)
#         else:
#             player_scores[player] = [score]
#
# print(player_scores)

player_scores = {}

with open("C:\\Users\crypt\OneDrive\Desktop\\scores.csv", "r") as f:
    for line in f:
        player, score = line.split(',')
        score = int(score)
        if player in player_scores:
            player_scores[player].append(score)
        else:
            player_scores[player] = [score]

for player, score_list in player_scores.items():
    min_score = min(score_list)
    max_score = max(score_list)
    avg_score = sum(score_list)/len(score_list)

    print(f'{player} ==> Min:{min_score}, Max:{max_score}, Avg:{avg_score}')