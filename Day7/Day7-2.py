file1 = open('Day7/Day7-Input.txt', 'r')
Lines = file1.readlines()
strengths = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
handStrengths = dict()

for line in Lines:
    split = line.replace("\n", "").split(" ")
    hand = split[0]
    bid = int(split[1])
    handStrength = dict()
    
    for strength in strengths:
        count = hand.count(strength)
        if count > 0:
            handStrength[strength] = count
    handStrengths[line.replace("\n", "")] = handStrength

fiveOAK = [] # 1
fourOAK = [] # 2
fullHouse = [] # 2
threeOAK = [] # 3
twoP = [] # 3
oneP = [] # 4
highC = [] # 5

strengths.reverse()
strengths.remove("J")
for handS in handStrengths:
    temp = handStrengths[handS]
    # Get joker amount
    jokers = 0
    if "J" in temp:
        jokers = temp["J"]
    highest = ""
    highestNum = 0
    for s in strengths:
        if s in temp:
            if temp[s] >= highestNum:
                highestNum = temp[s]
                highest = s
    if jokers == 5:
        temp["A"] = 5
    else:
        temp[highest] = temp[highest] + jokers
    if "J" in temp:
        temp.pop("J")

    # Add joker amount to biggest amount
    length = len(temp)
    # Five of a kind
    if length == 1:
        fiveOAK.append(handS)
    # Either full house or four of a kind
    elif length == 2:
        num = list(temp.values())[0]
        if num == 2 or num == 3:
            fullHouse.append(handS)
        else:
            fourOAK.append(handS)
    # Either three of a kind or two pairs
    elif length == 3:
        toak = False
        values = list(temp.values())
        for value in values:
            if value == 3:
                toak = True
        if toak == True:
            threeOAK.append(handS)
        else:
            twoP.append(handS)
    # One pair
    elif length == 4:
        oneP.append(handS)
    elif length == 5:
        highC.append(handS)


fiveOAK = sorted(fiveOAK, key=lambda x: x.split(" ")[0].replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "1").replace("T", "V"), reverse=True)
fourOAK = sorted(fourOAK, key=lambda x: x.split(" ")[0].replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "1").replace("T", "V"), reverse=True)
fullHouse = sorted(fullHouse, key=lambda x: x.split(" ")[0].replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "1").replace("T", "V"), reverse=True)
threeOAK = sorted(threeOAK, key=lambda x: x.split(" ")[0].replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "1").replace("T", "V"), reverse=True)
twoP = sorted(twoP, key=lambda x: x.split(" ")[0].replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "1").replace("T", "V"), reverse=True)
oneP = sorted(oneP, key=lambda x: x.split(" ")[0].replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "1").replace("T", "V"), reverse=True)
highC = sorted(highC, key=lambda x: x.split(" ")[0].replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "1").replace("T", "V"), reverse=True)
final = fiveOAK + fourOAK + fullHouse + threeOAK + twoP + oneP + highC
final.reverse()
answer = 0
for index, item in enumerate(final):
    answer += int(item.split(" ")[1]) * (index + 1)
print(answer)