def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().strip().split('\n')

    return data

class Head:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Tail:
    x = 0
    y = 0
    visitedPositions = {}
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visitedPositions = {}
    
    def isTouching(self, head):
        allowablePositions = {
        (self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y+1),
        (self.x, self.y-1), (self.x-1, self.y+1), (self.x-1, self.y-1), 
        (self.x+1, self.y-1), (self.x+1, self.y+1), (self.x, self.y)}
        return (head.x, head.y) in allowablePositions

    def locate(self, head):

        while( not self.isTouching(head)):
            if (head.x == self.x -1 and head.y == self.y -2):
                self.x -= 1
                self.y -= 1
            elif (head.x == self.x - 2 and head.y == self.y - 1):
                self.x -= 1
                self.y -= 1
            elif (head.x == self.x -1 and head.y == self.y + 2):
                self.x -= 1
                self.y += 1
            elif (head.x == self.x -2 and head.y == self.y + 1):
                self.x -= 1
                self.y += 1
            elif(head.x == self.x + 2 and head.y == self.y + 1):
                self.x += 1
                self.y += 1
            elif (head.x == self.x + 1 and head.y == self.y + 2):
                self.x += 1
                self.y += 1
            elif (head.x == self.x + 2 and head.y == self.y - 1):
                self.x += 1
                self.y -= 1
            elif (head.x == self.x + 1 and head.y == self.y - 2):
                self.x += 1
                self.y -= 1
            elif (head.x == self.x + 2 and head.y == self.y + 2):
                self.x += 1
                self.y += 1
            elif (head.x == self.x - 2 and head.y == self.y + 2):
                self.x -= 1
                self.y += 1
            elif (head.x == self.x - 2 and head.y == self.y - 2):
                self.x -= 1
                self.y -= 1
            elif (head.x == self.x + 2 and head.y == self.y - 2):
                self.x += 1
                self.y -= 1
            elif(head.x == self.x - 2):
                self.x -= 1
            elif (head.x == self.x + 2):
                self.x += 1
            elif (head.y == self.y - 2):
                self.y -= 1
            elif (head.y == self.y + 2):
                self.y += 1
            self.visitedPositions[(self.x, self.y)] = True

        self.visitedPositions[(self.x, self.y)] = True

def solveFirst(data):
    # (x,y) tuples for visited positions via the tail
    
    headKnot = Head(0,0)
    tailKnot = Tail(0,0)

    for line in data:
        [direction, distance] = line.split()
        distance = int(distance)
        match direction:
            case "R":
                for i in range(distance):
                    headKnot.x += 1
                    tailKnot.locate(headKnot)
            case "L":
                for i in range(distance):
                    headKnot.x -= 1
                    tailKnot.locate(headKnot)
            case "U":
                for i in range(distance):
                    headKnot.y += 1
                    tailKnot.locate(headKnot)
            case "D":
                for i in range(distance):
                    headKnot.y -= 1
                    tailKnot.locate(headKnot)
    print(len(tailKnot.visitedPositions))

def solveSecond(data):
    headKnot = Head(0, 0)
    links = [Tail(0, 0) for x in range(9)]


    for line in data:
        [direction, distance] = line.split()
        distance = int(distance)
        match direction:
            case "R":
                for i in range(distance):
                    headKnot.x += 1
                    links[0].locate(headKnot)
                    for j in range(1, 9):
                        links[j].locate(links[j-1])
            case "L":
                for i in range(distance):
                    headKnot.x -= 1
                    links[0].locate(headKnot)
                    for j in range(1, 9):
                        links[j].locate(links[j-1])
            case "U":
                for i in range(distance):
                    headKnot.y += 1
                    links[0].locate(headKnot)
                    for j in range(1, 9):
                        links[j].locate(links[j-1])
            case "D":
                for i in range(distance):
                    headKnot.y -= 1
                    links[0].locate(headKnot)
                    for j in range(1, 9):
                        links[j].locate(links[j-1])
    
    print(len(links[-1].visitedPositions))

if __name__ == "__main__":
    data = getInput("./input")
    solveFirst(data)
    solveSecond(data)