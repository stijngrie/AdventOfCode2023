file1 = open('Day2/Day2-Input.txt', 'r')
Lines = file1.readlines()

maxRed = 12
maxGreen = 13
maxBlue = 14
answer = 0


for line in Lines:
    failed = False
    #find gamenumber
    gameNumber = int(line.split(":")[0].split(" ")[1])
    grabs = line.split(":")[1].split(";") 
    for grab in grabs:
        colours = grab.split(",")
        for colour in colours: 
            if "red" in colour:
                red = int(colour.split(" ")[1])
                if maxRed < red: 
                    failed = True
            elif "green" in colour:
                green = int(colour.split(" ")[1])
                if maxGreen < green: 
                    failed = True 
            elif "blue" in colour:
                blue = int(colour.split(" ")[1])
                if maxBlue < blue: 
                    failed = True   
    if failed == False:
        answer += gameNumber
print(answer)        
        
                    
        
    
    
    
    
