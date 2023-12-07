from functools import reduce
from tqdm import tqdm
import time
import re
from math import sqrt, ceil, floor
from collections import Counter

def main():
    file_path_in = r"C:\Users\shahs\advent2023\data\daySeven.txt"

    with open(file_path_in, 'r') as file:
        content = file.read()

    # print(content)
    
    partOne(content.split("\n"))
    partTwo(content.split("\n"))
    

def convert(a):
    strength = ["A", "K", "Q", "T"] + list(map(str, range(9, 1, -1))) + ["J"]
    return 14 - strength.index(a)

def compareHand(hand, oldHand):
    counts = dict(Counter(hand))
    if len(counts) == 1:
        return tuple([7] + list(map(convert, oldHand)))
    elif len(counts) == 2:
        if set(counts.values()) == {4, 1}:
            return tuple([6] + list(map(convert, oldHand)))
        elif set(counts.values()) == {3, 2}:
            return tuple([5] + list(map(convert, oldHand)))
    elif len(counts) == 3:
        if set(counts.values()) == {3, 1, 1}:
            return tuple([4] + list(map(convert, oldHand)))
        elif set(counts.values()) == {2, 2, 1}:
            return tuple([3] + list(map(convert, oldHand)))
    elif len(counts) == 4:
        if set(counts.values()) == {2, 1, 1, 1}:
            return tuple([2] + list(map(convert, oldHand)))
    else:
        return tuple([1] + list(map(convert, oldHand)))
    
def strongestHand(hand):
    temp = []
    if "J" in hand:
        for s in (["A", "K", "Q", "T"] + list(map(str, range(9, 1, -1)))):
            temp.append(hand.replace("J", s))
    
        return compareHand(max(temp, key = lambda x: compareHand(x, hand)), hand)
    return compareHand(hand, hand)

def partOne(content):
    content = list(map(lambda x: x.split(), content))
    temp = sorted(content, key = lambda x: compareHand(x[0], x[0]))
    return (sum([(i+1)*int(k) for i, (j, k) in enumerate(temp)]))

def partTwo(content):
    content = list(map(lambda x: x.split(), content))
    temp = sorted(content, key = lambda x: strongestHand(x[0]))
    # print(strongestHand("8A7J7"))
    return (sum([(i+1)*int(k) for i, (j, k) in enumerate(temp)]))

if __name__ == "__main__":
    for i in tqdm(range(10000)):
        main()