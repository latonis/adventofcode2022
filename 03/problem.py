def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().strip().split('\n')

    return data

def solveFirst(data):
    for line in data:
        print(data)

if __name__ == "__main__":
    data = getInput("./test-input")
    solveFirst(data)