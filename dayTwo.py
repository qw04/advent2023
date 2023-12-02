import re
from collections import defaultdict
from functools import reduce

def product(lst):
  return reduce(lambda x, y: x*y, lst)

def main():
    file_path_in = r"C:\Users\shahs\advent2023\data\dayTwo.txt"

    with open(file_path_in, 'r') as file:
        content = file.read()

    content = content.split("\n")
    # partOne(content)
    # partTwo(content)

def partOne(content):
    sum = 0
    for i in range(len(content)):
        temp = list(map(lambda x: list(map(lambda y: y.strip(), x.split(","))), content[i].split(":")[1].split(";")))
        minCounter = defaultdict(lambda: 0)
        for stage in temp:
            for draw in stage:
                number, colour = draw.split(" ")
                minCounter[colour] = max(int(number), minCounter[colour])
        
        if minCounter["red"] < 13 and minCounter["green"] < 14 and minCounter["blue"] < 15:
            sum += i+1

    print(sum)

def partTwo(content):
    sum = 0
    for i in range(len(content)):
        temp = list(map(lambda x: list(map(lambda y: y.strip(), x.split(","))), content[i].split(":")[1].split(";")))
        minCounter = defaultdict(lambda: 0)
        for stage in temp:
            for draw in stage:
                number, colour = draw.split(" ")
                minCounter[colour] = max(int(number), minCounter[colour])

        sum += product(list(minCounter.values()))
        
    print(sum)


if __name__ == "__main__":
    main()