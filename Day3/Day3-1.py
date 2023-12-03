file1 = open('Day3/Day3-Input.txt', 'r')
Lines = file1.readlines()

specialChars = ['*', '-', '%', '/', '#', '&', '$', '=', '@', '+']
answer = 0

for y, line in enumerate(Lines):
    tempNumber = ''
    isValid = False
    for x, char in enumerate(line):
        if char.isnumeric():
            try:
                tempNumber = tempNumber + char
                if (Lines[y-1][x-1] in specialChars or Lines[y-1][x] in specialChars or Lines[y-1][x+1] in specialChars 
                    or Lines[y][x-1] in specialChars or Lines[y][x+1] in specialChars
                    or Lines[y+1][x-1] in specialChars or Lines[y+1][x] in specialChars or Lines[y+1][x+1] in specialChars):
                    isValid = True
            except IndexError:
                print("test")        
        else:
            if tempNumber != "":
                if isValid:
                    answer += int(tempNumber)
            tempNumber = ""
            isValid = False  
print(answer)     