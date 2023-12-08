from functools import reduce
from tqdm import tqdm
import time
import re
from math import sqrt, ceil, floor, lcm
from collections import Counter

def main():
    file_path_in = r"C:\Users\shahs\advent2023\data\dayEight.txt"

    with open(file_path_in, 'r') as file:
        content = file.read()

    # print(content)
    
    # partOne(content.split("\n\n"))
    partTwo(content.split("\n\n"))

def parsing(content):
    directions, graph = content
    graph = list(map(lambda x: x.split(" = "), graph.split("\n")))
    graph = {i: j[1:-1].split(", ") for i, j in graph}
    replace = lambda x: 0 if x == "L" else 1
    return list(map(replace, directions)), graph

def direction(directions):
    i = 0
    while True:
        yield directions[i%len(directions)]
        i += 1

def partOne(content):
    directions, graph = parsing(content)
    direction_gen = direction(directions)
    
    node = "AAA"
    count = 0

    while node != "ZZZ":
        # print(node)
        node = graph[node][next(direction_gen)]
        count += 1
    
    print(count)

def partTwo(content):
    directions, graph = parsing(content)
    direction_gen = direction(directions)

    nodes = list(filter(lambda x: x[-1] == "A", graph.keys()))
    n = len(nodes)
    count = 0
    cycleLength = []

    while len(nodes) > 0 :
        # print(nodes)
        count += 1
        direc = next(direction_gen)
        nodes = [graph[node][direc] for node in nodes]
        for node in nodes:
            if node[-1] == "Z":
                cycleLength.append(count)
                
        nodes = list(filter(lambda x: x[-1] != "Z", nodes))
        
    print(cycleLength)
    print(lcm(*cycleLength))

if __name__ == "__main__":
    main()