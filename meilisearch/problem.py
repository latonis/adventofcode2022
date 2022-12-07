from itertools import chain

class Node:
    def __init__(self):
        self.word = False
        self.children = [None, None]
        self.path = ""
        self.name = []
        self.stop = False

    def __str__(self):
        return f"{self.path}"

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
            runner = runner.children[idx]

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
            allNodes.append([node.path, " ".join(node.name), stopCount])

        if (all(node.children)):
            stopCount +=1

        if node.children[0]:
            self.findPaths(node.children[0], stopCount, allNodes)

        if node.children[1]:
            self.findPaths(node.children[1], stopCount, allNodes)

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

    for node in results:
        path = node[0]
        name = node[1]
        stops = node[2]

        if not shortest:
            shortest = [[stops, name, path]]
            continue
        if (stops < shortest[0][0]):
            shortest = [[stops, name, path]]
            continue
        if (stops == shortest[0][0]):
            shortest.append([stops, name, path])
    results.sort(key=lambda x: x[2])
    # print(results)
    print(shortest)
if __name__ == "__main__":
    data = getInput("./input")
    solveOne(data)
    solveTwo(data)