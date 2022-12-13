from itertools import chain

class Node:
    def __init__(self):
        self.word = False
        self.children = [None, None]
        self.path = ""
        self.name = []
        self.stop = False
        self.parent = None
        self.key = ""
    def __str__(self):
        return f"{self.name}"

    def __iter__(self):
        "implement the iterator protocol"
        for v in chain(*map(iter, self.children)):
            yield v
        yield self.value

class NodeList:
    # lexicographically sorting via L has priority over R
    nodes = []
    prefixes = {}
    def __init__(self):
        self.root = Node()    
        self.root.path = "ROOT"
    def toIndex(self, char):
        if (char == "L"):
            return 0
        else:
            return 1


    def addNode(self, key, name):
        runner = self.root
        n = len(key)

        for height in range(n):
            idx = self.toIndex(key[height])
            if not (runner.children[idx]):
                runner.children[idx] = Node()
            parent = runner
            runner = runner.children[idx]
            runner.parent = parent
            runner.key = key[height]

        runner.word = True
        runner.name.append(name)
        runner.path = key

    def __str__(self):
        return str([str(x) for x in self.nodes])

    def findPaths(self, node, stopCount, allNodes):
        if (node.word):
            allNodes.append((node, stopCount))

        if (all(node.children)):
            stopCount +=1

        if node.children[0]:
            self.findPaths(node.children[0], stopCount, allNodes)
        
        if node.children[1]:
            self.findPaths(node.children[1], stopCount, allNodes)
    
    def nextShortest(self, node, stopCount):
        if (node is None):
            return None, stopCount
    
        if all(node.children) or node.word:
            stopCount +=  1 
        elif (node.word and any(node.children)):
            stopCount +=  1 
        
        if (node.word):
            return node, stopCount

        if (node.children[0] is not None and node.children[1] is not None):
            stopCountLeft = 0
            stopCountRight = 0
            [nodeL, stopCountRight] = self.nextShortest(node.children[0], stopCountLeft)
            [nodeR, stopCountLeft] = self.nextShortest(node.children[1], stopCountRight)   
            
            if (stopCountLeft <= stopCountRight):
                return nodeL, stopCountLeft
            else:
                return nodeR, stopCountRight
        elif node.children[0] is not None:
            return self.nextShortest(node.children[0], stopCount)
        elif node.children[1] is not None:
            return self.nextShortest(node.children[1], stopCount)
        else:
            node = self.removeNode(node, id(node))
            return self.nextShortest(node.parent, stopCount)

    def removeNode(self, node, id_):        
        if (id_ == id(node)):
            if (node.children[0] is not None and node.children[1] is not None):
                node.word = False
                return node
            if (node.parent is not None):
                if (node.key == "L"):
                    node.parent.children[0] = None
                else:
                    node.parent.children[1] = None
            return node
        
        if node.children[0]:
            if (self.removeNode(node.children[0], id_)):
                return node
        if node.children[1]:
            if (self.removeNode(node.children[1], id_)):
                return node
        return None
def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().strip().split('\n')

    return data

def solveOne(data):
    nodes = NodeList()

    for line in data:
        [name, path] = line.split(" - ")
        nodes.addNode(path, name)
    
    results = []
    nodes.findPaths(nodes.root, 0, results)
    shortest = []

    for node, stopCount in results:
        path = node.path
        name = node.name

        if not shortest:
            shortest = [[stopCount, name, path]]
            continue
        if (stopCount < shortest[0][0]):
            shortest = [[stopCount, name, path]]
            continue
        if (stopCount == shortest[0][0]):
            shortest.append([stopCount, name, path])

    print(shortest[0])

def solveTwo(data):
    nodes = NodeList()

    for line in data:
        [name, path] = line.split(" - ")
        nodes.addNode(path, name)
    
    results = []
    nodes.findPaths(nodes.root, 0, results)
    shortest = []

    for node, stopCount in results:
        if not shortest:
            shortest = [[node, stopCount]]
            continue
        if (stopCount < shortest[0][1]):
            shortest = [[node, stopCount]]
            continue
        if (stopCount == shortest[0][1]):
            shortest.append([node, stopCount])

    totalStopCount = 0
    node = shortest[0][0]
    
    while (node is not None):
        if (node.word):
            print(node.name)
            node = nodes.removeNode(nodes.root, id(node))
        [node, nextStop] = nodes.nextShortest(node, 0)
        print(nextStop)
        totalStopCount += nextStop

    print(totalStopCount)

if __name__ == "__main__":
    data = getInput("./test-input")
    solveOne(data)
    solveTwo(data)