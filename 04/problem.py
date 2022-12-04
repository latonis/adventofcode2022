def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().strip().split('\n')

    return data

# i need to solve this arithmetically, this is so slow lol
def solveFirst(data):
    ranges = []
    count = 0
    for line in data:
        splitRes = line.split(',')
        first = splitRes[0].split('-')
        second = splitRes[1].split('-')
        startFirst = int(first[0])
        endFirst = int(first[1])
        startSecond = int(second[0])
        endSecond = int(second[1])
        firstRange = [x for x in range(startFirst, endFirst+1)]
        secondRange = [x for x in range(startSecond, endSecond+1)]
        if (all(elem in firstRange for elem in secondRange)) or all(elem in secondRange for elem in firstRange):
            count+=1
    print(count)
        # print("".join([x for x in range(first[0], int(first[1]))]))

# i need to solve this arithmetically, this is so slow lol
def solveSecond(data):
    ranges = []
    count = 0
    for line in data:
        splitRes = line.split(',')
        first = splitRes[0].split('-')
        second = splitRes[1].split('-')
        startFirst = int(first[0])
        endFirst = int(first[1])
        startSecond = int(second[0])
        endSecond = int(second[1])
        firstRange = [x for x in range(startFirst, endFirst+1)]
        secondRange = [x for x in range(startSecond, endSecond+1)]
        if (any(elem in firstRange for elem in secondRange)) or any(elem in secondRange for elem in firstRange):
            count+=1
    print(count)

if __name__ == "__main__":
    data = getInput("./input")
    solveFirst(data)
    solveSecond(data)