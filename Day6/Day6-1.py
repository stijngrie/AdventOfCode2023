file1 = open('Day6/Day6-Input.txt', 'r')
Lines = file1.readlines()
 
times = Lines[0].replace("\n", "").split(":")[1].split(" ")
times = list(filter(lambda x: x != "", times))
distances = Lines[1].replace("\n", "").split(":")[1].split(" ")
distances = list(filter(lambda x: x != "", distances))

answer = 0
for index, time in enumerate(times):
    winAmount = 0
    for x in range(0, int(time) + 1):
        if x * (int(time) - x) > int(distances[index]):
            winAmount += 1
    if answer == 0:
        answer = winAmount
    else:
        answer *= winAmount
print(answer)