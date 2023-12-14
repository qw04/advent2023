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
    file_path_in = r"C:\Users\shahs\advent2023\data\dayThirteen.txt"

    with open(file_path_in, 'r') as file:
        content = file.read()


    # partOne(content)
    partTwo(content)

def func(content):
    content = content.split("\n")
    n = len(content) - 1
    print(content)
    for i in range(n):
        print(content[max(2*i + 1 - n, 0): i+1])
        print(content[min(2*i + 1, n): i:-1])

        if content[max(2*i + 1 - n, 0): i+1] == content[min(2*i + 1, n):i:-1]:
            print("the one above this")
            return i
        print()
    return -1

def symDif(lst1, lst2):
    return [[i, j] for i, j in zip(lst1, lst2) if i!=j]

def func2(content):
    content = content.split("\n")
    n = len(content) - 1
    # print(content)
    for i in range(n):
        # print(content[max(2*i + 1 - n, 0): i+1])
        # print(content[min(2*i + 1, n): i:-1])
        temp = symDif(content[max(2*i + 1 - n, 0): i+1], content[min(2*i + 1, n):i:-1])
        # print(temp, 1)
        if len(temp) == 1 and len(symDif(*temp[0])) == 1:
            # print(symDif(*temp[0]), 2)
            # print("the one above this")
            # print()
            return i
        # print()
    return -1

def partOne(content):
    content = content.split("\n\n")
    left, up = 0, 0
    for smallContent in content: 
        newSmallContent = "\n".join(list(map(lambda x:"".join(x), np.array([list(row) for row in smallContent.split("\n")]).T.tolist())))
        temp1, temp2 = func(smallContent), func(newSmallContent)
        print(temp1, temp2)
        up += temp1 + 1 if temp1 != -1 else 0
        left += temp2 + 1 if temp2 != -1 else 0

    print(up*100 + left)

def partTwo(content):
    content = content.split("\n\n")
    left, up = 0, 0
    for smallContent in content: 
        newSmallContent = "\n".join(list(map(lambda x:"".join(x), np.array([list(row) for row in smallContent.split("\n")]).T.tolist())))
        temp1, temp2 = func2(smallContent), func2(newSmallContent)
        # print(temp1, temp2)
        up += temp1 + 1 if temp1 != -1 else 0
        left += temp2 + 1 if temp2 != -1 else 0

    print(up*100 + left)



if __name__ == "__main__":
    main()
