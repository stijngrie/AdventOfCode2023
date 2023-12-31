file1 = open('Day4/Day4-Input.txt', 'r')
Lines = file1.readlines()

answer = 0

for line in Lines:
    winningNumbers = line.replace("\n", "").split(":")[1].split("|")[0].split(" ")
    winningNumbers = list(filter(lambda x: x != '', winningNumbers))
    scratchNumbers = line.replace("\n", "").split(":")[1].split("|")[1].split(" ")
    scratchNumbers = list(filter(lambda x: x != '', scratchNumbers))

    winAmount = 0
    for number in scratchNumbers:
        if number in winningNumbers:
            if winAmount == 0:
                winAmount += 1
            else:
                winAmount *= 2
    answer += winAmount
print(answer)