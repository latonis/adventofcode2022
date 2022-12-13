def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().strip().split('\n')

    return data


def nextSteps(heatmap, currentPos) -> list:
    path = []

    x = currentPos[0]
    y = currentPos[1]
    rowN = len(heatmap)
    colN = len(heatmap[0])
    currentElevation = ord('a') if ord(heatmap[x][y]) == ord('S') else ord(heatmap[x][y])
    
    nextElevation = ord('z') if currentElevation == ord('z') else currentElevation + 1

    if (x > 0):
        if ord(heatmap[x-1][y]) <= nextElevation:
            path.append((x-1,y))
    if (x < rowN - 1):
        if ord(heatmap[x+1][y]) <= nextElevation:
            path.append((x+1,y))
    if (y > 0):
        if ord(heatmap[x][y-1]) <= nextElevation:
            path.append((x,y-1))
    if (y < colN - 1):
        if ord(heatmap[x][y+1]) <= nextElevation:
            path.append((x,y+1))

    return path

def myDijkstra(heatmap, currentPath, visited, goal):
    while (currentPath):
        for node, steps in currentPath:
            nextStepArr = nextSteps(heatmap, node)
            for step in nextStepArr:
                if step == goal:
                    return steps + 1

                if (step in visited.keys()):
                    continue

                visited[step] = True
                currentPath.append((step, steps+1))
        currentPath.pop(0)
    return False


def solveFirst(data):
    heatmap = []
    visited = {}
    startPos = (0, 0)
    endPos = (0,0)

    for idx, line in enumerate(data):
        row = []
        for idx2, char in enumerate(line):
            if (char == "S"):
                startPos = (idx, idx2)
                visited[startPos] = True
            elif (char == "E"):
                char = "z"
                endPos = (idx, idx2)
            row.append(char)
        heatmap.append(row)
    
    print(myDijkstra(heatmap, [(startPos, 0)], visited, endPos))
 

def solveSecond(data):
    heatmap = []
    startPositions = []
    endPos = (0,0)

    for idx, line in enumerate(data):
        row = []
        for idx2, char in enumerate(line):
            if (char in ["a", "S"]):
                startPositions.append((idx, idx2))
            elif (char == "E"):
                char = "z"
                endPos = (idx, idx2)
            row.append(char)
        heatmap.append(row)

    results = []
    for start in startPositions:
        results.append(myDijkstra(heatmap, [(start, 0)], {start: True}, endPos))

    print(min([x for x in results if x is not False]))
    
if __name__ == "__main__":
    data = getInput("./input")
    solveFirst(data)
    solveSecond(data)