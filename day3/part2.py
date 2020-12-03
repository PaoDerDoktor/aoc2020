from typing import List, Dict, Tuple


with open("day3/input.txt") as inputFile:
    data: List[List[str]] = [[ch for ch in line.strip()] for line in inputFile.readlines()]
    
    x: int = 0
    y: int = 0
    slopes: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]] = (
        (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)
    )
    trees: int = 0
    
    for slope in slopes:
        counter = 0
        while y < len(data):
            line = data[y]
            
            if line[x] == '#':
                counter += 1
            x = (x+slope[0]) % len(line)
            y += slope[1]
        if trees == 0:
            trees = counter
        else:
            trees *= counter
        x = 0
        y = 0
    
    print(trees)