file1 = open('Day4/Day4-Input.txt', 'r')
Lines = file1.readlines()

for line in Lines:
    winningNumbers = line.split(":")[1].split("|")[0].split(" ")
    print(winningNumbers)