def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().strip()

    return data

def solveFirst(data):
    n = len(data)
    for idx in range(4, n):
        chars = data[idx-4:idx]
        if (len(set(chars))== 4):
            print(chars, idx)
            return

def solveSecond(data):
    n = len(data)
    for idx in range(14, n):
        chars = data[idx-14:idx]
        if (len(set(chars))== 14):
            print(chars, idx)
            return

if __name__ == "__main__":
    data = getInput("./input")
    solveFirst(data)
    solveSecond(data)