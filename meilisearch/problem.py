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

    # def compareNodes(self, node1, node2):
    #     # node 1 less than node 2
    #     for char1, char2 in zip(node1.path, node2.path):
    #         if (char1 == char2):
    #             continue
    #         elif (char1 == "L"):
    #             return -1
    #         else:
    #             return 1
    #     return 0

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
            return
        print(node.path)

        if any(node.children):
            stopCount +=  1
        
        if (node.word):
            return node
        stopCountLeft = -1
        stopCountRight = -1
        elif node.children[0]:
            print("LEFT")
            if (node.children[1]):
                print("BOTH SIBLINGS")
                if (not node.children[0].word and node.children[1].word):
                    return node.children[1]
            return self.nextShortest(node.children[0], stopCount)
        elif node.children[1]:
            
            print("RIGHT")
            return self.nextShortest(node.children[1], stopCount)
        else:
            print("PARENT")
            self.removeNode(node, id(node))
            return self.nextShortest(node.parent, stopCount)

    def removeNode(self, node, id_):
        print()
        
        if (id_ == id(node)):
            print("FOUND")
            if (node.children[0] is not None and node.children[1] is not None):
                node.word = False
                return
            if (node.parent is not None):
                if (node.key == "L"):
                    node.parent.children[0] = None
                else:
                    node.parent.children[1] = None
            return
        
        if node.children[0]:
            self.removeNode(node.children[0], id_)
        if node.children[1]:
            self.removeNode(node.children[1], id_)
        
        
    
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
    shortestName = ""

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
    shortestName = ""

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
            nodes.removeNode(nodes.root, id(node))
        node = nodes.nextShortest(node.parent, totalStopCount)

    print(totalStopCount)

if __name__ == "__main__":
    data = getInput("./test-input")
    solveOne(data)
    solveTwo(data)