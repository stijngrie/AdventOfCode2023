file1 = open('Day6/Day6-Input.txt', 'r')
Lines = file1.readlines()
 
time = int(Lines[0].replace("\n", "").split(":")[1].replace(" ", ""))
distance = int(Lines[1].replace("\n", "").split(":")[1].replace(" ", ""))

answer = 0
for x in range(0, int(time) + 1):
    if x * (time - x) > distance:
        answer += 1
print(answer)