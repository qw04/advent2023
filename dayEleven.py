from functools import reduce
from tqdm import tqdm
import time
import re
from math import sqrt, ceil, floor, lcm
from collections import Counter, deque, defaultdict
import numpy as np


def main():
    file_path_in = r"C:\Users\shahs\advent2023\data\dayEleven.txt"

    with open(file_path_in, 'r') as file:
        content = file.read()


    # partOne(content)
    partTwo(content, 1000000)


def partOne(content):
    rowStretch = []
    for row in content.split("\n"):
        rowStretch.append([row] * (1 + int("#" not in row)))
    
    rowStretch = reduce(lambda x, y: x + y, rowStretch)

    allStretch = []
    for column in range(len(rowStretch[0])):
        temp = "".join([row[column] for row in rowStretch])
        allStretch.append([temp] * (1 + int("#" not in temp)))

    allStretch = np.array([list(row) for row in reduce(lambda x, y: x + y, allStretch)]).T.tolist()

    counter = 0
    galaxies = []
    for i in range(len(allStretch)):
        for j in range(len(allStretch[0])):
            if allStretch[i][j] == "#":
                allStretch[i][j] = str(counter)
                galaxies.append((i, j))
                counter += 1

    dit = {}
    for i, (a, b) in enumerate(galaxies):
        for j, (m, n) in enumerate(galaxies):
            if i != j:
                dit[(min(i, j), max(i, j))] = abs(a-m) + abs(b-n)


    print(sum(dit.values()))
    
def partTwo(content, var):
    rowStretch = []
    for row in content.split("\n"):
        if "#" in row: rowStretch.append(row)
        else: rowStretch.append("x" * len(row))
    
    
    allStretch = []
    for column in range(len(rowStretch[0])):
        temp = "".join([row[column] for row in rowStretch])
        if "#" in temp: allStretch.append(temp)
        else: allStretch.append("x" * len(temp))

    allStretch = np.array([list(row) for row in allStretch]).T.tolist()


    counter = 1
    iCount = 0
    galaxies = []

    for i in range(len(allStretch)):
        if "x" == allStretch[i][0]: 
            iCount += (var - 1)
        
        jCount = 0
        for j in range(len(allStretch[0])):
            
            if allStretch[i][j] == "x":
                jCount += (var - 1)

            if allStretch[i][j] == "#":
                allStretch[i][j] = str(counter)
                galaxies.append((i + iCount, j + jCount))
                # print(i, iCount, j, jCount, len(galaxies))
                counter += 1
    
    # for i in allStretch:
    #     print("".join(i))

    # print(galaxies)

    dit = {}
    for i, (a, b) in enumerate(galaxies):
        for j, (m, n) in enumerate(galaxies):
            if i != j:
                dit[(min(i, j), max(i, j))] = abs(a-m) + abs(b-n)

    # print(dit[(0, 6)])

    print(sum(dit.values()))

if __name__ == "__main__":
    main()
