from functools import cmp_to_key

def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().strip().split('\n\n')

    return data

def intoList(left, right):
    if (type(left) != type(right)):
        if (type(left) != list):
            left = [left]
        else:
            right = [right]
    if (type(left) == list and type(right) == list):
        for i in range(len(left)):
            if (i < len(right)):
                result = intoList(left[i], right[i])
                if (result != 0):
                    return result
        if (len(left) > len(right)):
            return -1
        if (len(left) == len(right)):
            return 0
        return 1
       
    if (type(left) == int and type(right) == int):
        if (left > right):
            return -1
        if (left == right):
            return 0
    return 1

def solveFirst(data):
    total = 0
    runningIndex = 1
    for idx, line in enumerate(data):
        results = line.split("\n")
        left = eval(results[0])
        right = eval(results[1])
        res = intoList(left, right)

        if (res == 1):
            total += idx + 1
        runningIndex += 2

    print(total)

def solveSecond(data):
    total = 0
    runningIndex = 1
    packets = [[[2]], [[6]]]

    for idx, line in enumerate(data):
        results = line.split("\n")
        left = eval(results[0])
        right = eval(results[1])
        packets.append(left)
        packets.append(right)

    packets.sort(key=cmp_to_key(intoList), reverse=True)
    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
if __name__ == "__main__":
    data = getInput("./input")
    solveFirst(data)
    solveSecond(data)