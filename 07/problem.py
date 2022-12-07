def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().strip().split('\n')

    return data


class directory:
    files = []
    childDirectories = []
    def __init__(self):
        self.childDirectories = []
        self.files = []

class item:
    size = 0
    def __init__(self, size):
        self.size = size

def dirSum(directory, maxSize=False):
    totalSize = 0

    for item in directory.files:
        totalSize += item.size
    

    for childDir in directory.childDirectories:
        totalSize += dirSum(childDir, maxSize)

    return totalSize

def solveFirst(data):
    commands = []
    directories = {}
    currDir = ""
    for idx, line in enumerate(data):
        splitRes = line.split()
        if (splitRes[0] == "$"):
            commands.append(splitRes[1:])
            # print(line)
            if (splitRes[1] == "cd"):
                if (not currDir):
                    currDir = splitRes[2]
                elif (splitRes[2] == ".."):
                    n = len(currDir.split("/"))
                    currDir = "/".join(currDir.split("/")[:n-2]) + "/"
                else:
                    currDir += splitRes[2] + "/"
            elif (splitRes[1] == "ls"):
                pass
        else:
            # print(splitRes)
            if (currDir not in directories.keys()):
                directories[currDir] = directory()
            if (not splitRes[0].isalpha()):
                size = int(splitRes[0])
                fileinDir = item(size)
                directories[currDir].files.append(fileinDir)
            else:
                if (splitRes[0] == "dir"):
                    childDir = currDir + splitRes[1] + "/"
                    if (childDir not in directories.keys()):
                        directories[childDir] = directory()
                    directories[currDir].childDirectories.append(directories[childDir])
    
    toDeleteSize = 0
    print(directories.keys())
    for dirr in directories:
        res = dirSum(directories[dirr], True)
        if (res <= 100000):
            toDeleteSize += res
    print(toDeleteSize)

def solveSecond(data):
    totalSpace = 70000000
    unusedSpace = 30000000
    commands = []
    directories = {}
    currDir = ""
    
    for idx, line in enumerate(data):
        splitRes = line.split()
        if (splitRes[0] == "$"):
            commands.append(splitRes[1:])
            # print(line)
            if (splitRes[1] == "cd"):
                if (not currDir):
                    currDir = splitRes[2]
                elif (splitRes[2] == ".."):
                    n = len(currDir.split("/"))
                    currDir = "/".join(currDir.split("/")[:n-2]) + "/"
                else:
                    currDir += splitRes[2] + "/"
            elif (splitRes[1] == "ls"):
                pass
        else:
            # print(splitRes)
            if (currDir not in directories.keys()):
                directories[currDir] = directory()
            if (not splitRes[0].isalpha()):
                size = int(splitRes[0])
                fileinDir = item(size)
                directories[currDir].files.append(fileinDir)

            else:
                if (splitRes[0] == "dir"):
                    childDir = currDir + splitRes[1] + "/"
                    if (childDir not in directories.keys()):
                        directories[childDir] = directory()
                    directories[currDir].childDirectories.append(directories[childDir])

    dirSizes = []

    for dirr in directories:
        res = dirSum(directories[dirr], False)
        dirSizes.append(res)
    
    usedSpace = dirSizes[0]
    
    dirSizes.sort()
    print(dirSizes)
    print(f"Needed Space: {unusedSpace}")
    usedSpace = dirSum(directories["/"])
    print(f"Used Space: {usedSpace}")
    freeSpace = totalSpace - usedSpace
    print(f"Free Space: {freeSpace}")

    for size in dirSizes:
        if (freeSpace + size >= unusedSpace):
            print(freeSpace + size)
            print(size)
            return
    
if __name__ == "__main__":
    data = getInput("./input")
    solveFirst(data)
    solveSecond(data)