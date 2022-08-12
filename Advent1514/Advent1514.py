puzzle_input = "input.txt"

reindeer_distance = dict()
reindeer_list = list()
reindeer_speed = dict()
reindeer_stamina = dict()
reindeer_rest = dict()
reindeer_isMoving = dict()
reindeer_timeLeft = dict()
reindeer_score = dict()

total_time = 2503

with open(puzzle_input) as f:
    for line in f:
        word = line.split()
        reindeer_list.append(word[0])
        
        reindeer_speed[word[0]] = int(word[3])
        reindeer_stamina[word[0]] = int(word[6])
        reindeer_rest[word[0]] = int(word[13])
        reindeer_distance[word[0]] = 0
        reindeer_score[word[0]] = 0
        reindeer_isMoving[word[0]] = True
        reindeer_timeLeft[word[0]] = reindeer_stamina[word[0]]



for i in range(total_time):
    for j in range(len(reindeer_list)):
        if reindeer_isMoving[reindeer_list[j]]:
            reindeer_distance[reindeer_list[j]] += reindeer_speed[reindeer_list[j]]
            reindeer_timeLeft[reindeer_list[j]] -= 1
            if reindeer_timeLeft[reindeer_list[j]] == 0:
                reindeer_isMoving[reindeer_list[j]] = False
                reindeer_timeLeft[reindeer_list[j]] = reindeer_rest[reindeer_list[j]]
        else:
            reindeer_timeLeft[reindeer_list[j]] -= 1
            if reindeer_timeLeft[reindeer_list[j]] == 0:
                reindeer_timeLeft[reindeer_list[j]] = reindeer_stamina[reindeer_list[j]]
                reindeer_isMoving[reindeer_list[j]] = True

    reindeer_score[max(reindeer_distance, key=reindeer_distance.get)] += 1

print(reindeer_score)