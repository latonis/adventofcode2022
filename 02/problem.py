def getInput(file):
    data = None

    with open(file) as f:
        data = f.read().strip().split('\n')

    return data

def solveFirst(data):
    # rock is a and x, 
    # paper is b and Y
    # scissors is c and z
    
    # a beats y
    wins = {("A", "Y"), ("B", "Z"), ("C", "X")}
    losses = {("A", "Z"), ("B", "X"), ("C", "Y")}
    
    scores = {"X": 1, "Y": 2, "Z": 3}
    score = 0
    for line in data:
        given, answer = line.split()
        score += scores[answer]
        if (given, answer) in wins:
            score += 6
        elif (given, answer) in losses:
            score += 0
        else:
            score += 3
    print(score)

def solveSecond(data):
    wins = {"A": "Y", "B": "Z", "C": "X"}
    losses = {"A": "Z", "B": "X", "C": "Y"}
    
    scores = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}
    
    score = 0

    for line in data:
        given, answer = line.split()
        if (answer == 'X'):
            score += 0
            score += scores[losses[given]]
        elif (answer == 'Y'): 
            score += 3
            score += scores[given]
        else:
            score += 6
            score += scores[wins[given]]
    print(score)


if __name__ == "__main__":
    data = getInput("input")
    solveFirst(data)
    solveSecond(data)