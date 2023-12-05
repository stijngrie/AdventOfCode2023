file1 = open('Day4/Day4-Input.txt', 'r')
Lines = file1.readlines()

cards = dict()

for index, line in enumerate(Lines):
    cards[index+1] = line

for index, line in enumerate(Lines):
    winningNumbers = line.replace("\n", "").split(":")[1].split("|")[0].split(" ")
    winningNumbers = list(filter(lambda x: x != '', winningNumbers))
    scratchNumbers = line.replace("\n", "").split(":")[1].split("|")[1].split(" ")
    scratchNumbers = list(filter(lambda x: x != '', scratchNumbers))

    winAmount = 0
    for number in scratchNumbers:
        if number in winningNumbers:
            winAmount += 1

    cardNumber = int(line.split(":")[0].replace("Card ", ""))

    for number in range(1, winAmount+1):
        Lines.append(cards[cardNumber + number])
print(len(Lines))