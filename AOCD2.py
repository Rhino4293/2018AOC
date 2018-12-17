from collections import Counter

def getData(filename):
    with open(filename,"r") as files:
        return (files.readlines())

def part1(inData):
    two =0
    three =0
    for twos in inData:
        counts = Counter(Counter(twos).values())
        if 2 in counts:
            two += 1
        if 3 in counts:
            three +=1
    return (two*three)

def part2(inData):
    for w in inData:
        print(w)

inputData = getData("AOCD2.txt")
#print(part1(inputData))
print(part2(inputData))