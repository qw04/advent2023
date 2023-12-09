from functools import reduce
from tqdm import tqdm
import time
import re
from math import sqrt, ceil, floor, lcm
from collections import Counter
import numpy as np
from scipy import odr

def main():
    file_path_in = r"C:\Users\shahs\advent2023\data\dayNine.txt"

    with open(file_path_in, 'r') as file:
        content = file.read()


    # partOne(content.split('\n'))
    partTwo(content.split('\n'))

def model(row, i):
    poly_model = odr.polynomial(i)
    data = odr.Data(list(range(len(row.split()))), list(map(int, row.split())))
    odr_obj = odr.ODR(data, poly_model)
    output = odr_obj.run()
    poly = np.poly1d(output.beta[::-1])
    return poly(len(row.split()))

def func(temp):
    print(temp)
    if temp == [0] * len(temp):
        return 0
    else:
        temp = list(map(lambda x : temp[x+1] - temp[x], range(len(temp)-1)))
        a = func(temp)
        print(temp[-1], a)
        return temp[-1] + a

def partOne(content):
    sum = 0
    for row in content:
        temp = list(map(int, row.split()))
        sum += func(temp)+temp[-1]
        # sum += int(round(model(row, counter), 0))

    print(sum)
        

def func2(temp):
    # print(temp)
    if temp == [0] * len(temp):
        return 0
    else:
        temp = list(map(lambda x : temp[x] - temp[x-1], range(1, len(temp))))
        return temp[0] - func2(temp)


def partTwo(content):
    sum = 0
    for row in content:
        temp = list(map(int, row.split()))
        # print(temp[0] - func2(temp))
        sum += (temp[0] - func2(temp))
        # sum += int(round(model(row, counter), 0))
    print(sum)






if __name__ == "__main__":
    main()