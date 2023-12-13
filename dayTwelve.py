from functools import reduce
from tqdm import tqdm
import time
import re
from math import sqrt, ceil, floor, lcm
from collections import Counter, deque, defaultdict
import numpy as np
from itertools import product
from functools import cache


def main():
    file_path_in = r"C:\Users\shahs\advent2023\data\dayTwelve.txt"

    with open(file_path_in, 'r') as file:
        content = file.read()


    # partOne(content)
    partTwo(content)


def func(counts, nums, seq):
    count = 0
    for perm in product(["#", "."], repeat=len(nums)):
        for i in range(len(nums)):
            seq[nums[i]] = perm[i]
        sol = []
        temp = 0
        for i in range(len(seq)):
            if seq[i] == "#":
                temp += 1
            elif seq[i] == "." and temp != 0:
                sol.append(temp)
                temp = 0
        if temp != 0: sol.append(temp)

        if sol == counts:
            count += 1
        
    return count

def partOne(content):
    content = list(map(lambda x: x.split(" "), content.split("\n")))
    sum = 0
    for row in tqdm(content):
        seq = list(row[0])
        nums = []
        for i in range(len(seq)):
            if seq[i] == "?": 
                nums.append(i)
        counts = list(map(int, row[1].split(",")))

        sum += func(counts, nums, seq)

    print(sum)

@cache
def func2(counts, seq, count):
    # print()
    # print(counts, seq, count)
    counts = list(counts)
    if len(seq) == 0:
        # print(1)
        return len(counts) == 0 or (len(counts) == 1 and counts[0] == count)
    if seq[0] == "?":
        # print(2)
        return func2(tuple(counts), "#" + seq[1:], count) + func2(tuple(counts), "." + seq[1:], count)
    elif seq[0] == "#":
        # print(3)
        if not counts:
            return 0
        elif count + 1 > counts[0]:
            return 0
        return func2(tuple(counts), seq[1:], count + 1)

    elif seq[0] == ".":
        # print(4)
        if not counts:
            return func2(tuple(counts), seq[1:], 0)
        elif not count:
            return func2(tuple(counts), seq[1:], 0)
        elif count == counts[0]:
            return func2(tuple(counts[1:]), seq[1:], 0)
        elif count != counts[0]:
            return 0


def partTwo(content):
    content = list(map(lambda x: x.split(" "), content.split("\n")))
    sum = 0

    for row in content:
        seq = (row[0] + "?") * 5
        counts = list(map(int, row[1].split(","))) * 5
        # print(seq[:-1])
        # print(counts)
        temp = func2(tuple(counts), seq[:-1], 0)
        # print(temp)
        # print()

        sum += temp
    print(sum)
 

if __name__ == "__main__":
    main()
