def loadInstructions():
    instructions = []

    with open('../inputs/day5.txt', 'r') as instructionFile:
        line = instructionFile.readline()

        while line:
            instructions.append(int(line[:-1]))
            line = instructionFile.readline()

    return instructions


def walkInstructionList(instructions, useOddBehaviour=False):
    currentPosition = 0
    stepCount = 0

    while 0 <= currentPosition < len(instructions):
        instruction = instructions[currentPosition]

        if useOddBehaviour:
            if instruction >= 3:
                instructions[currentPosition] -= 1
            else:
                instructions[currentPosition] += 1
        else:
            instructions[currentPosition] += 1

        stepCount += 1
        currentPosition += instruction

    return stepCount


def main():
    instructions = loadInstructions()
    # instructions = [0, 3, 0, 1, -3]

    print(walkInstructionList(instructions.copy()))
    print(walkInstructionList(instructions.copy(), useOddBehaviour=True))


if __name__ == '__main__':
    main()
