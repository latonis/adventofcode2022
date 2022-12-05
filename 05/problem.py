import re

def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().split('\n\n')

    return data

def parseCrates(data):
    crates = []
    # figure this out eventually

def solveFirst(data):
    # stacks = [["N", "Z"], ["D", "C", "M"], ["P"]]
    stacks = [["T", "R", "D", "H", "Q", "N", "P", "B"], ["V", "T", "J", "B", "G", "W"], ["Q", "M", "V", "S", "D", "H", "R", "N"], ["C", "M", "N", "Z", "P"], ["B", "Z", "D"], ["Z", "W", "C", "V"], ["S", "L", "Q", "V", "C", "N", "Z", "G"], ["V", "N", "D", "M", "J", "G", "L"], ["G", "C", "Z", "F", "M", "P", "T"]]
    crateStack = parseCrates(data[0])
    for line in data[1].split('\n'):
        print(line)
        times, posFrom, posTo = re.match(r'[^0-9.]*(\d*)[^0-9.]*(\d*)[^0-9.]*(\d*)', line).groups()
        posFrom = int(posFrom)
        posTo = int(posTo)
        posFrom -= 1
        posTo -= 1
        print(times, posFrom, posTo)
        for i in range(int(times)):
            stacks[posTo].insert(0, stacks[posFrom].pop(0))
            print(stacks)
    print("".join([x[0] for x in stacks]))

def solveSecond(data):
    # stacks = [["N", "Z"], ["D", "C", "M"], ["P"]]
    stacks = [["T", "R", "D", "H", "Q", "N", "P", "B"], ["V", "T", "J", "B", "G", "W"], ["Q", "M", "V", "S", "D", "H", "R", "N"], ["C", "M", "N", "Z", "P"], ["B", "Z", "D"], ["Z", "W", "C", "V"], ["S", "L", "Q", "V", "C", "N", "Z", "G"], ["V", "N", "D", "M", "J", "G", "L"], ["G", "C", "Z", "F", "M", "P", "T"]]
    crateStack = parseCrates(data[0])
    for line in data[1].split('\n'):
        print(line)
        times, posFrom, posTo = re.match(r'[^0-9.]*(\d*)[^0-9.]*(\d*)[^0-9.]*(\d*)', line).groups()
        times = int(times)
        posFrom = int(posFrom)
        posTo = int(posTo)
        posFrom -= 1
        posTo -= 1
        print(times, posFrom, posTo)
        for i in range(int(times)):
            stacks[posTo].insert(i, stacks[posFrom].pop(0))
            print(stacks)
    print("".join([x[0] for x in stacks]))

if __name__ == "__main__":
    data = getInput("input")
    # solveFirst(data)
    solveSecond(data)