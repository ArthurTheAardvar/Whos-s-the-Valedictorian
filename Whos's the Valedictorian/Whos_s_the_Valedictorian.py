import math

cases = int(input()) 

for i in range(cases): #go through the other lines
    line = input()
    
    line = line.split(" ") #split up the line by spaces
    line[0] = int(line[0])
    x = line[0]
    y = line[1]
    
    d = math.sqrt(pow(x,2) + pow(y,2))

    print(d)