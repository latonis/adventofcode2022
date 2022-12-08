def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().strip().split('\n')

    return data

def printMap(treeMap):
    idx = 0
    for i in treeMap:
        for j in i:
            print(j, end=" ")
        print()

def calcScenicScore(row, col, treeMap):
    rightScore = 0
    leftScore  = 0
    upScore = 0
    downScore = 0

    for i in range(col+1, len(treeMap[row])):
        if (treeMap[row][col] > treeMap[row][i]):
            rightScore += 1
        else:
            rightScore += 1
            break
    
    # look left
    for i in range(col-1, -1, -1):
        if (treeMap[row][col] > treeMap[row][i]):
            leftScore += 1
        else:
            leftScore += 1
            break
    # look up

    for i in range(row-1, -1, -1):
        if (treeMap[row][col] > treeMap[i][col]):
            upScore += 1
        else:
            upScore += 1
            break

    for i in range(row+1, len(treeMap)):
        if (treeMap[row][col] > treeMap[i][col]):
            downScore += 1
        else:
            downScore += 1
            break
    
    return rightScore * leftScore * upScore * downScore

def isVisible(row, col, treeMap):
    visibleRight = True
    visibleLeft = True
    visibleUp = True
    visibleDown = True

    # look right
    for i in range(col+1, len(treeMap[row])):
        if (treeMap[row][col] <= treeMap[row][i]):
            visibleRight = False
    # look left
    for i in range(col-1, -1, -1):
        if (treeMap[row][col] <= treeMap[row][i]):
            visibleLeft = False
    # look up
    for i in range(row-1, -1, -1):
        if (treeMap[row][col] <= treeMap[i][col]):
            visibleUp = False
    # look right
    for i in range(row+1, len(treeMap[row])):
        if (treeMap[row][col] <= treeMap[i][col]):
            visibleDown = False

    return visibleUp or visibleDown or visibleLeft or visibleRight

def solveFirst(data):
    treeMap = []
    visible = 0
    for line in data:
        row = []
        for tree in line:
            row.append(tree)
        treeMap.append(row)
    
    alwaysVisI = [0, len(treeMap[0])-1]
    alwaysVisJ = [0, len(treeMap[0])-1]
    for i in range(len(treeMap)):
        for j in range(len(treeMap[i])):
            if (i in alwaysVisI or j in alwaysVisJ):
                visible += 1
            else:
                if(isVisible(i, j, treeMap)):
                    visible += 1
    print(visible)

def solveSecond(data):
    treeMap = []
    visible = 0
    for line in data:
        row = []
        for tree in line:
            row.append(tree)
        treeMap.append(row)
    
    alwaysVisI = [0, len(treeMap[0])-1]
    alwaysVisJ = [0, len(treeMap[0])-1]
    maxScore = 0
    for i in range(len(treeMap)):
        for j in range(len(treeMap[i])):
            res = calcScenicScore(i, j, treeMap)
            if (res > maxScore):
                maxScore = res
    
    print(maxScore)

if __name__ == "__main__":
    data = getInput("./input")
    solveFirst(data)
    solveSecond(data)