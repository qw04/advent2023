import re

file_path_in = r"C:\Users\shahs\advent2023\data\dayOne.txt"

with open(file_path_in, 'r') as file:
    content = file.read()

def func(string):
    match1 = re.search(f"\d|{'|'.join(letter)}", string).group(0)
    match2 = re.search(f"\d|{'|'.join(reverseLetter)}", string[::-1]).group(0)
    if match1 in letter: match1 = letter.index(match1) + 1
    if match2 in reverseLetter: match2 = reverseLetter.index(match2) + 1
    re.purge()
    return match1, match2

sum = 0
letter = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
reverseLetter = [i[::-1] for i in letter]

content = content.split("\n")

for i in range(len(content)):
    match1, match2 = func(content[i])
    
    sum += int(match1)*10 + int(match2)

print(sum)
    