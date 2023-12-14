from functools import reduce
from tqdm import tqdm
import time
import re
from math import sqrt, ceil, floor, lcm
from collections import Counter, deque, defaultdict
import numpy as np
from itertools import product
from functools import cache, lru_cache
from copy import deepcopy
from queue import PriorityQueue

def main():
    file_path_in = r"C:\Users\shahs\advent2023\data\dayFourteen.txt"

    with open(file_path_in, 'r') as file:
        content = file.read()


    # partOne(content)
    partTwo(content)

def tilt(line):
    freeSpaceQueue = PriorityQueue()
    ballIndex = []
    newLine = line.copy()
    for i in range(len(line)+1):
        if i != len(line) and line[i] == ".":
            freeSpaceQueue.put(i)

        elif i != len(line) and line[i] == "O":
            ballIndex.append(i)

        elif i == len(line) or line[i] == "#":
            counter = 0
            
            if freeSpaceQueue.empty():  continue
            else: current = freeSpaceQueue.get()

            for ball in ballIndex:
                if current < ball:
                    newLine[current], newLine[ball] = newLine[ball], newLine[current]
                    freeSpaceQueue.put(ball)
                    
                    if freeSpaceQueue.empty():  continue
                    else: current = freeSpaceQueue.get()

            ballIndex = []
            freeSpaceQueue = PriorityQueue()

    return newLine



def partOne(content):
    content = np.array(list(map(list, content.split("\n")))).T.tolist()
    para = []
    mysum = 0
    for line in content:
        newLine = tilt(line)
        para.append(newLine)
        # mysum += sum([i+1 for i, j in enumerate(newLine[::-1]) if j == "O"])
    
    para = np.array(para).T.tolist()
    print(g(para))
    para = "\n".join(list(map(lambda x: "".join(x), para)))
    # print(para)
    


def cycle(para):
    para = np.array(para).T.tolist()
    para = list(map(tilt, para))
    para = np.array(para).T.tolist()

    para = list(map(tilt, para))
    
    para = [i[::-1] for i in np.array(para).T.tolist()]
    para = list(map(tilt, para))
    para = np.array([i[::-1] for i in para]).T.tolist()
    

    para = [i[::-1] for i in para]
    para = list(map(tilt, para))
    para = [i[::-1] for i in para]
    return para

def f(para):
    para = np.array(list(map(tilt, np.array(para).T.tolist()))).T.tolist()
    return g(para)

def g(para):
    sum_ = 0
    for i, line in enumerate(para):
        sum_ += line.count("O") * (len(para) - i)
        # print(line.count("O"), len(para) - i)
    return sum_

def partTwo(content):
    content = list(map(list, content.split("\n")))
    theFourHorseman = content

    for _ in tqdm(range(1000)):
        
        theFourHorseman = cycle(theFourHorseman)
        a = tuple(map(tuple, theFourHorseman))

    print(g(theFourHorseman))
    # print("\n".join(list(map(lambda x: "".join(x), theFourHorseman))))
    # print()

    
    

if __name__ == "__main__":
    main()