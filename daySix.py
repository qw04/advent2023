from functools import reduce
from tqdm import tqdm
import time
import re
from math import sqrt, ceil, floor

def main():
    file_path_in = r"C:\Users\shahs\advent2023\data\daySix.txt"

    with open(file_path_in, 'r') as file:
        content = file.read()

    # print(content)
    # partOne(content.split("\n"))
    partTwo(content.split("\n"))

def partOne(content):
    time = list(map(int, content[0].split(":")[1].split()))
    distance = list(map(int, content[1].split(":")[1].strip().split()))


    lower = lambda y, s: ceil(((y/2) - sqrt(((y**2) / 4) - s - 0.000001)))
    upper = lambda y, s: floor(((y/2) + sqrt(((y**2) / 4) - s - 0.000001)))

    
    print(reduce(lambda a, b : a*b, [upper(y, s) - lower(y, s) + 1 for y,s in zip(time, distance)]))

def partTwo(content):
    lower = lambda y, s: ceil(((y/2) - sqrt(((y**2) / 4) - s - 0.000001)))
    upper = lambda y, s: floor(((y/2) + sqrt(((y**2) / 4) - s - 0.000001)))

    time = int("".join(content[0].split(":")[1].split()))
    distance = int("".join(content[1].split(":")[1].split()))

    print(time, distance)

    print(upper(time, distance) - lower(time, distance) + 1)

if __name__ == "__main__":
    main()