from collections import defaultdict

def main():
    file_path_in = r"C:\Users\shahs\advent2023\data\dayFour.txt"

    with open(file_path_in, 'r') as file:
        content = file.read()

    content = content.split("\n")
    # print(content)
    # partOne(content)
    partTwo(content)

def partOne(content):
    sum = 0
    for card in content:
        numbers = card.split(":")[1]
        win, mine = list(map(lambda x: x.strip().split(" "), numbers.split("|")))
        while "" in win: win.remove("")
        while "" in mine: mine.remove("")
        point = 0.5
        for i in mine:
            if i in win:
                point *= 2
        # print(point)
        sum += point if point != 0.5 else 0
        # print(sum)
    print(int(sum))

def func(matches):
    numberCalls = [1]*len(matches)
    for i in range(len(matches)):
        for j in range(1, min(matches[i]+1, len(matches)-i-1)):
            numberCalls[i+j] += numberCalls[i]
        # print(numberCalls)
    return sum(numberCalls)


def partTwo(content):
    sum = 0
    matches = [None] * len(content)
    for index, card in enumerate(content):
        numbers = card.split(":")[1]
        win, mine = list(map(lambda x: x.strip().split(" "), numbers.split("|")))
        while "" in win: win.remove("")
        while "" in mine: mine.remove("")
        point = 0
        for i in mine:
            if i in win:
                point += 1
        # print(point)
        matches[index] = point
        # print(sum)
    
    print(func(matches))

if __name__ == "__main__":
    main()