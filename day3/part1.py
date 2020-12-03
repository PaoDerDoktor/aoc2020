from typing import List


with open("day3/input.txt") as inputFile:
    data: List[List[str]] = [[ch for ch in line.strip()] for line in inputFile.readlines()]
    
    x: int = 0
    trees: int = 0
    
    for line in data:
        if line[x] == '#':
            line[x] = 'O'
            trees += 1
        else:
            line[x] = 'X'
        x = (x+3) % len(line)
    
    print(trees)