file1 = open('Day2/Day2-Input.txt', 'r')
Lines = file1.readlines()

answer = 0

for line in Lines:
    highestRed = 0
    highestGreen = 0
    highestBlue = 0
    gameNumber = int(line.split(":")[0].split(" ")[1])
    grabs = line.split(":")[1].split(";")
    for grab in grabs:
        colours = grab.split(",")
        for colour in colours: 
            if "red" in colour:
                red = int(colour.split(" ")[1])
                if highestRed < red:
                    highestRed = red
            elif "green" in colour:
                green = int(colour.split(" ")[1])
                if highestGreen < green:
                    highestGreen = green
            elif "blue" in colour:
                blue = int(colour.split(" ")[1])
                if highestBlue < blue:
                    highestBlue = blue
    answer += highestRed * highestGreen * highestBlue

print(answer)        
        
                    
        
    
    
    
    
