from typing import List


with open('day1/input.txt', 'r') as inFile:
    data: List[int] = [int(line) for line in inFile.readlines()]
    
    i:int = 0
    j:int = 0
    
    found:bool = False
    
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i]+data[j] == 2020:
                found = True
                break
        if found:
            break
        
    print(data[i]*data[j])