def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().strip().split('\n')

    return data

def signalStrengthCalc(cycleCount, x_register, modValue):
    if (cycleCount % modValue) == 20:
                signalStrength = cycleCount * x_register
                return signalStrength
    return 0

def drawSprite(cycleCount, spritePos):
    if cycleCount > 0:
        if ((cycleCount % 40) in spritePos):
            print("#", end='')
        else:
            print('.', end='')
        
        if (cycleCount % 40 == 0 and cycleCount > 0):
            print(cycleCount)

def solveFirst(data):
    cycleCount = 0
    x_register = 1
    cycles = {"addx": 2, "noop": 1}
    modValue = 40
    signalStrengthSum = 0
    for line in data:
        op = line.split()
        instr = op[0]
        if (instr == "noop"):
            cycleCount += 1
            signalStrengthSum += signalStrengthCalc(cycleCount, x_register, modValue)
        elif (instr == "addx"):
            for i in range(cycles[instr]):
                cycleCount += 1
                signalStrengthSum += signalStrengthCalc(cycleCount, x_register, modValue)
            x_register += int(op[1])
        else:
            print(f"Oops! Unknown Instruction: {instr}")
    print(signalStrengthSum)
    
def solveSecond(data):
    cycleCount = 0
    x_register = 1
    cycles = {"addx": 2, "noop": 1}
    for line in data:
        op = line.split()
        instr = op[0]
        if (instr == "noop"):
            spritePosition = {x_register-1, x_register, x_register+1}
            drawSprite(cycleCount, spritePosition)  
            cycleCount += 1
            # signalStrengthSum += signalStrengthCalc(cycleCount, x_register, modValue)
        elif (instr == "addx"):
            for i in range(cycles[instr]):
                spritePosition = {x_register-1, x_register, x_register+1}
                drawSprite(cycleCount, spritePosition)

                cycleCount += 1
                # signalStrengthSum += signalStrengthCalc(cycleCount, x_register, modValue)
            x_register += int(op[1])
        else:
            print(f"Oops! Unknown Instruction: {instr}")
if __name__ == "__main__":
    data = getInput("./input")
    solveFirst(data)
    solveSecond(data)