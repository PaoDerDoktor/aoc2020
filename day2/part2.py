from typing import List, Tuple

with open('day2/input.txt', 'r') as inputFile:
    data: List[Tuple[Tuple[int, int], str, str]] = [((int(line.split(': ')[0].split(' ')[0].split('-')[0]),
                                                      int(line.split(': ')[0].split(' ')[0].split('-')[1])),
                                                     line.split(': ')[0].split(' ')[1],
                                                     line.split(':')[1].strip()) for line in inputFile.readlines()]
    
    valids: int = 0
    for entry in data:
        if (entry[2][entry[0][0]-1]==entry[1]) ^ (entry[2][entry[0][1]-1]==entry[1]):
            valids += 1
            
    print(valids)