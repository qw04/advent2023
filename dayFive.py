from functools import reduce
from tqdm import tqdm
import time
import re

def main():
    file_path_in = r"C:\Users\shahs\advent2023\data\dayFive.txt"

    with open(file_path_in, 'r') as file:
        content = file.read()

    # print(content)
    # partOne(content.split("\n"))
    partTwo(content)

def convert(content, seeds):
    # assume that translations can't shift back
    newSeeds = []
    for seed in seeds:
        flag = False

        for index, (i, j, k) in enumerate(content):
            # print(seed)
            # print(range(j, j+k))
            if seed in range(j, j+k): 
                newSeed, flag = seed - j + i, True
            elif seed < j:
                if index == 0: newSeed, flag = seed, True
                else: newSeed, flag = seed - oj + oi, True
            
            oi, oj, ok = i, j, k
            
            if flag: break

            
        if seed > content[-1][1] + content[-1][2] - 1 and not flag:
            newSeed = seed
        
        newSeeds.append(newSeed)
    
    return newSeeds



def partOne(content):
    # seeds = list(map(int, content[0].split(":")[1].split(" ")[1:]))
    seeds = [3366565397]
    # print(seeds)
    counter = -2

    for index, line in enumerate(content[1:]):
        if index + 1 == len(content) - 1 or ("map" in content[index+1] and index != 1):
            lst = content[index - counter + 1:index+2*(index + 1 == len(content) - 1)]
            temp = list(map(lambda x:list(map(int, x.split(" "))), lst))
            temp.sort(key=lambda x:x[1])
            seeds = convert(temp, seeds)
            # print(seeds)
            counter = 0

        else: counter += 1

    print(seeds)

def convert_(content, seed):
    # assume that translations can't shift back
    flag = False

    for index, (i, j, k) in enumerate(content):
        if seed in range(i, i+k): 
            newSeed, flag = seed - i + j, True
            # print(newSeed, "1", (i, j, k))
        elif seed < i:
            if index == 0: 
                newSeed, flag = seed, True
                # print(newSeed, "2")
            else: 
                newSeed, flag = seed - oi + oj, True
                # print(newSeed, "3")
            
        oi, oj, ok = i, j, k
            
        if flag: break

            
    if seed > content[-1][1] + content[-1][2] - 1 and not flag:
        newSeed = seed

    return newSeed

def entireConvert(content, seed):
    counter = -1
    # print(seed)

    for index, line in enumerate(content[:-1]):
        # print(index, line)
        if "map" in content[index+1] and index == 1:
            temp = list(map(lambda x:list(map(int, x.split(" "))), content[:index+1]))
            temp.sort(key=lambda x:x[0])
            seed, counter = convert_(temp, seed), 0
            # print(seed, content[:index+1])

        elif "map" in content[index+1] and index != len(content):
            lst = content[index - counter + 2 : index+1]
            temp = list(map(lambda x:list(map(int, x.split(" "))), lst))
            temp.sort(key=lambda x:x[0])
            seed, counter = convert_(temp, seed), 0
            # print(seed, temp)

        else: counter += 1
    return seed

def splitInterval(row, x, y):
    intervals = set()
    q = set([(x, y)])
    while q:
        # time.sleep(2)
        i, j = q.pop()
        flag = False
        for a, b, c in row:
            if flag: break
            if b > i and b+c-1 < j:
                # print(1)
                q.add((i, b-1))
                q.add((b+c, j))
                intervals.add((b, b+c-1))
                flag = True
                
        
            elif b <= i and b+c-1 < j and b+c-1 >= i:
                # print(2)
                intervals.add((i, b+c-1))
                q.add((b+c, j))
                flag = True
                

            elif b > i and b+c-1 >= j and b <= j:
                # print(3)
                intervals.add((b, j))
                q.add((i, b-1))
                flag = True
            
            elif b+c-1 < i or b > j:
                # print(4)
                pass
                # intervals.add((i, j))
                # flag = True
            
            # print(a, b, c)
            # print(i, j)
            # print(q)
            # print(intervals)
            # print("")

        if not flag:
            # print(5)
            intervals.add((i, j))

        

    return list(intervals)

def check(intervals, val):
    for i, j in intervals:
        if val in range(i, j+1):
            print(range(i, j))

def partTwo(content):
    seeds = list(map(int, content.split("\n")[0].split(":")[1].split(" ")[1:]))
    intervals = [(i, i+j-1) for i, j in zip(seeds[::2], seeds[1::2])]
    # print(list(map(lambda x: entireConvert(content[:1:-1], x), seeds)))
    check(intervals, 1409419462)
    concat = lambda x : reduce(lambda a, b: a+b, x)
    
    temp = list(map(lambda x:x.split("\n")[1:], content.split("\n\n")[1:]))
    temp = list(map(lambda x: [list(map(int, y.split())) for y in x], temp))

    # print(convert(sorted([[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]], key=lambda x:x[1]), [61, 70]))
    # print(splitInterval([[60, 56, 37], [56, 93, 4]], 90, 99))

    for conversion in temp:
        # print(intervals)
        intervals = concat([splitInterval(conversion, x, y) for x, y in intervals])
        # print(intervals)
        # print(conversion)
        intervals = [convert(sorted(conversion, key=lambda x:x[1]), y) for y in intervals]
        # print(intervals)
        # print("")

    # print(intervals)
    # print("\n")
    print(min(intervals, key=lambda x: min(x)))


if __name__ == "__main__":
    main()

