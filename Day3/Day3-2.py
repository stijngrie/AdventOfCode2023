file1 = open('Day3/Day3-Input.txt', 'r')
Lines = file1.readlines()

answer = 0
gears = dict()

for y, line in enumerate(Lines):
    tempNumber = ''
    isValid = False
    gearLocation = ""
    for x, char in enumerate(line):
        if char.isnumeric():
            try:
                tempNumber = tempNumber + char
                for i in range(-1, 2):
                   for j in range(-1, 2):    
                       if y + i > 0 and x + j > 0 and Lines[y + i][x + j] == "*":
                           isValid = True
                           gearLocation = str(x+j) + ',' + str(y+i)
            except IndexError:
                False == False 
        else:
            if tempNumber != "":
                if isValid:
                    if gearLocation in gears:
                        gears[gearLocation].append(tempNumber)
                    else:
                        gears[gearLocation] = []
                        gears[gearLocation].append(tempNumber)
            tempNumber = ""
            isValid = False
            gearLocation = ""
for gear in gears:
    mult = 0
    if len(gears[gear]) > 1:
        for number in gears[gear]:
            if mult == 0:
                mult = int(number)
            else:
                mult *= int(number)
    answer += mult
print(answer) 