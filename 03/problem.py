def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().strip().split('\n')

    return data

def solveFirst(data):
    bothComp = []
    for line in data:
        firstHalf = set(line[:len(line)//2])
        secondHalf = set(line[(len(line)//2):])
        bothComp.append(*firstHalf.intersection(secondHalf))
    score = 0
    for char in bothComp:
        if (char.islower()):
            score += ord(char)% 96
        else:
            score += ord(char)% 64 + 26
    print(f"Priority for first part: {score}")

def solveSecond(data):
    bothComp = []
    count = 0
    for i in range(0, len(data), 3):
        firstInt = set(data[i]).intersection(set(data[i+1]))
        bothComp.append(*firstInt.intersection((data[i+2])))

    score = 0
    for char in bothComp:
        if (char.islower()):
            score += ord(char)% 96
        else:
            score += ord(char)% 64 + 26
    print(f"Priority for second part: {score}")

if __name__ == "__main__":
    data = getInput("./input")
    solveFirst(data)
    solveSecond(data)