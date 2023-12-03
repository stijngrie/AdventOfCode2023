# Open input file
file1 = open('Day1/Day1-Input.txt', 'r')
Lines = file1.readlines()
 
answer = 0
# Loop over every line
for line in Lines:
    firstnumber = ""
    lastnumber = 0
    for char in line:
        if char.isnumeric() and firstnumber == "":
            firstnumber = char
            lastnumber = char
        elif char.isnumeric():
            lastnumber = char
    lineNum = str(firstnumber) + str(lastnumber)
    answer += int(lineNum)
print(answer)