import operator
import math
ops = {"+":operator.add, "-":operator.sub, "*": operator.mul, "/":operator.floordiv, "divisible": operator.mod}
monkeys = []

class Monkey:
    items = []
    operation = None
    toTrue = None
    toFalse = None
    a = None
    b = None
    testOp = None
    testVal = None
    inspectionCount = 0
    worry = False
    gcd = 1

    def __init__(self, items, operator, toTrue, toFalse, a, b, testOp, testVal, worry):
        self.items = items
        self.operator = operator
        self.toTrue = toTrue
        self.toFalse = toFalse
        self.a = a
        self.b = b
        self.testOp = ops[testOp]
        self.testVal = testVal
        self.worry = worry
        self.gcd = 1

    def applyOperator(self, a, b):
        return ops[self.operator](a, b)

    def turn(self):
        for idx in range(len(self.items)):
            if (self.a =="old"):
                if (self.b == "old"):
                    self.items[idx] = self.applyOperator(self.items[idx], self.items[idx])
                else:
                    self.items[idx] = self.applyOperator(self.items[idx], int(self.b))
            else:
                self.items[idx] = self.applyOperator(int(self.a), int(self.b))
            
            if (self.worry):
                self.items[idx] = self.items[idx] // 3

            self.inspectionCount += 1
            self.test(self.items[idx])
            
        self.items = []

    def test(self, item):
        if (self.testOp(item, self.testVal) == 0):
            monkeys[self.toTrue].items.append(item)
        else:
            monkeys[self.toFalse].items.append(item)



def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().strip().split('\n')

    return data

def solveFirst(data):
    global monkeys
    monkeys = []
    for i in range(len(data)):
        if (data[i].startswith("Monkey")):
            monkeyIdx = int(data[i].split()[1].replace(":", ''))
            itemsArr = list(map(lambda s: int(s.replace(",", "")), data[i+1].split()[2:]))
            [a, operator, b] = data[i+2].split()[3:]
            testOp = data[i+3].split()[1]
            testVal = int(data[i+3].split()[3])
            toTrue = int(data[i+4].split()[5])
            toFalse = int(data[i+5].split()[5])
            monkeys.append(Monkey(itemsArr, operator, toTrue, toFalse, a, b, testOp, testVal, True))

    for i in range(20):
        for monkey in monkeys:
            monkey.turn()
    
    monkeys.sort(key=lambda s: s.inspectionCount, reverse=True)

    monkeyBusiness = monkeys[0].inspectionCount * monkeys[1].inspectionCount
    print(monkeyBusiness)

def solveSecond(data):
    global monkeys
    monkeys = []

    for i in range(len(data)):
        if (data[i].startswith("Monkey")):
            monkeyIdx = int(data[i].split()[1].replace(":", ''))
            itemsArr = list(map(lambda s: int(s.replace(",", "")), data[i+1].split()[2:]))
            [a, operator, b] = data[i+2].split()[3:]
            testOp = data[i+3].split()[1]
            testVal = int(data[i+3].split()[3])
            toTrue = int(data[i+4].split()[5])
            toFalse = int(data[i+5].split()[5])
            monkeys.append(Monkey(itemsArr, operator, toTrue, toFalse, a, b, testOp, testVal, False ))
    
    rounds = [1, 20, 1000]

    for i in range(10000):
        for idx, monkey in enumerate(monkeys):
            if (i in rounds):
                print(f"Monkey {idx} inspected {monkey.inspectionCount} items")
            monkey.turn()

    monkeys.sort(key=lambda s: s.inspectionCount, reverse=True)

    
    monkeyBusiness = monkeys[0].inspectionCount * monkeys[1].inspectionCount
    print(monkeyBusiness)

if __name__ == "__main__":
    data = getInput("./test-input")
    solveFirst(data)
    solveSecond(data)