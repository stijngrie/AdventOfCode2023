numbersText = ["one", "1", "two", "2", "three", "3", "four","4" , "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9"]
numbers = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

file1 = open('Day1/Day1-Input.txt', 'r')
Lines = file1.readlines()
 
answer = 0
# Loop over every line
for line in Lines:
    firstnumber = ""
    lastnumber = ""
    firstNumberIndex = 9999
    lastNumberIndex = -1
    for number in numbersText:
        # First number
        temp = line.find(number)
        if temp >= 0 and temp < firstNumberIndex:
            firstNumberIndex = temp
            firstnumber = number
        # Last number
        temp2 = line.rfind(number)
        if temp2 >= 0 and temp2 > lastNumberIndex:
            lastNumberIndex = temp2
            lastnumber = number
    if len(firstnumber) > 1:
        firstnumber = numbers.index(firstnumber)
    if len(lastnumber) > 1:
        lastnumber = numbers.index(lastnumber)
    lineNum = str(firstnumber) + str(lastnumber)
    answer += int(lineNum)
    print(lineNum)
print(answer);