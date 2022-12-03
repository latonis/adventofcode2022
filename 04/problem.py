def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().strip().split('\n')

    return data

def solveFirst(data):
    for line in data:
        print(line)

def solveSecond(data):
    for line in data:
        print(line)

if __name__ == "__main__":
    data = getInput("./test-input")
    solveFirst(data)
    solveSecond(data)