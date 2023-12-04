from functools import reduce

def main():
    file_path_in = r"C:\Users\shahs\advent2023\data\dayThree.txt"

    with open(file_path_in, 'r') as file:
        content = file.read()

    content = content.split("\n")
    # print(content)
    # partOne(content)
    partTwo(content)

def check(number, content, i, j):
        a = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
        for j in range(j, j+len(str(number))):
            for x, y in a:
                try:
                    if content[x+i][y+j] in ['+', '&', '$', '#', '*', '%', '/', '-', '@', '=']:
                        # print(number)
                        return number
                    
                except IndexError:
                    pass
        
        return 0

def partOne(content):
    content = list(map(lambda row: list(row), content))
    flag = False
    number = 0
    sum = 0

    for i, row in enumerate(content):
        
        for j, cell in enumerate(row):
            
            if cell.isdigit() and not flag:
                number = int(cell)
                flag = True
                start = [i, j]

            elif cell.isdigit(): 
                number = ((number*10) + int(cell))
            
            elif flag:
                sum += check(number, content, *start)
                flag = False
                number = 0
    
    if flag: sum += check(number, content, *start)
    

    print(sum)

def findNumber(content, i, j):
    
    if content[i][j].isdigit():
        try:
            x, y = j, j
            while content[i][y].isdigit():
                y+=1

            while content[i][x].isdigit():
                x-=1

            return (int("".join(content[i][x+1:y])), (x+1, y-1))
        
        except IndexError:
            return (int("".join(content[i][x+1:y])), x+1, y-1)
        
    return 1

def checkGear(content, i, j):
    a = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
    product = 1
    toMult = set()
    for x, y in a:
        try:
            pass
            toMult.add(str(findNumber(content, x+i, y+j)))
            # print(findNumber(content, x+i, y+j))
            # toMult.add(str((num, m, n)))
        except IndexError:
            pass


    toMult = toMult.difference(['1'])
    if len(list(toMult)) < 2:
        return 0
    else:
        return reduce(lambda x, y: x*y, list(map(lambda x: eval(x)[0], list(toMult))))

def partTwo(content):
    content = list(map(lambda row: list(row), content))
    sum = 0

    for i, row in enumerate(content):
        for j, cell in enumerate(row):
            if cell == "*":
                sum += checkGear(content, i, j)
    print(sum)

if __name__ == "__main__":
    main()