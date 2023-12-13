from functools import reduce
from tqdm import tqdm
import time
import re
from math import sqrt, ceil, floor, lcm
from collections import Counter, deque, defaultdict
import numpy as np


def main():
    file_path_in = r"C:\Users\shahs\advent2023\data\dayTen.txt"

    with open(file_path_in, 'r') as file:
        content = file.read()


    # partOne(content)
    partTwo(content)

def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))

def bfs(graph, i, j):
    # answer = []
    visited, queue = set(), deque([((), i, j)])
    visited.add(((), i, j))

    while queue:

        # Dequeue a vertex from queue
        path, i, j = queue.popleft()
        # print(i, j, queue)

        # If not visited, mark it as visited, and
        # enqueue it

        if i in range(len(graph)) and j in range(len(graph[i])) and graph[i][j] != []:
            for x, y in graph[i][j]:
                ni, nj = y+i, x+j
                if (ni, nj) in [(b, c) for _, b, c in visited]: 
                    yield len(path)
                elif (path, ni, nj) not in [(a, b, c) for a, b, c in visited]:
                    queue.append((tuple(list(path) + [(i, j)]), ni, nj))
                    visited.add((tuple(list(path) + [(i, j)]), ni, nj))
                else:
                    # print(ni, nj, "visited")
                    pass
            # print(queue)
            # print()
    # return answer

def partOne(content):
    dit = {
        "|": [(0, 1), (0, -1)],
        "-": [(-1, 0), (1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(0, 1), (-1, 0)],
        "F": [(0, 1), (1, 0)],
        ".": [],
        "S": [(0, 1), (0, -1), (1, 0), (-1, 0)]
    }
    
    

    for i, row in enumerate(content.split("\n")):
        try:
            iStart, jStart = i, row.index("S")
        except ValueError:
            pass
    
    content = list(map(lambda x: list(map(lambda y:dit[y], x)), content.split('\n')))
    graph = defaultdict(lambda : [])
    for i, row in enumerate(content):
        for j, cell in enumerate(row):
            for x, y in cell:
                # print(i, j, x, y)
                if y+i in range(len(content)) and x+j in range(len(content[0])):
                    graph[(i, j)].append((y+i, x+j))
    
    # for i in graph:
        # print(i,graph[i])
    
    temp = float("-inf")
    for i in dfs(graph, (iStart, jStart), (iStart, jStart)):
        temp = max(len(i), temp)
    print(temp//2)


def is_point_in_path(x, y, cycle) -> bool:
    num = len(cycle)
    j = num - 1
    c = False
    for i in range(num):
        if (x == cycle[i][0]) and (y == cycle[i][1]):
            return True
        if (cycle[i][1] > y) != (cycle[j][1] > y):
            slope = (x - cycle[i][0]) * (cycle[j][1] - cycle[i][1]) - (cycle[j][0] - cycle[i][0]) * (y - cycle[i][1])
            if slope == 0:
                return True
            if (slope < 0) != (cycle[j][1] < cycle[i][1]):
                c = not c
        j = i
    return c



def partTwo(content):
    dit = {
        "|": [(0, 1), (0, -1)],
        "-": [(-1, 0), (1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(0, 1), (-1, 0)],
        "F": [(0, 1), (1, 0)],
        ".": [],
        "S": [(0, 1), (0, -1), (1, 0), (-1, 0)]
    }
    
    for i, row in enumerate(content.split("\n")):
        try:
            iStart, jStart = i, row.index("S")
        except ValueError:
            pass
    oldContent = content.split("\n")
    content = list(map(lambda x: list(map(lambda y:dit[y], x)), oldContent))
    graph = defaultdict(lambda : [])
    for i, row in enumerate(content):
        for j, cell in enumerate(row):
            for x, y in cell:
                # print(i, j, x, y)
                if y+i in range(len(content)) and x+j in range(len(content[0])):
                    graph[(i, j)].append((y+i, x+j))
    
    # for i in graph:
        # print(i,graph[i])
    
    temp = float("-inf")
    for i in dfs(graph, (iStart, jStart), (iStart, jStart)):
        if len(i) > temp:
            temp, maxCycle = len(i), i
    print(temp)
    sum = 0
    for i, row in tqdm(list(enumerate(oldContent))):
        for j, cell in enumerate(row):
            if is_point_in_path(i, j, maxCycle):
                sum += 1
        
    print(sum - len(maxCycle))


if __name__ == "__main__":
    main()




