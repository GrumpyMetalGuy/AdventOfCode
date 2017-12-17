def loadBlockConfiguration():
    blocks = []

    with open('../inputs/day6.txt', 'r') as blockFile:
        line = blockFile.readline()

        while line:
            blocks.append(int(line[:-1]))
            line = blockFile.readline()

    return blocks


def redistributeBlocks(blocks):
    stepCount = 0
    seenBlocks = dict()

    while True:
        stepCount += 1

        blockIndex = blocks.index(max(blocks))
        currentBlockCount = blocks[blockIndex]
        blocks[blockIndex] = 0

        for blockOffset in range(1, currentBlockCount + 1):
            blocks[(blockIndex + blockOffset) % len(blocks)] += 1

        blockTuple = tuple(blocks)

        if blockTuple in seenBlocks:
            return stepCount - seenBlocks[blockTuple]
        else:
            seenBlocks[blockTuple] = stepCount


def main():
    blocks = loadBlockConfiguration()
    # blocks = [0, 2, 7, 0]

    print(redistributeBlocks(blocks.copy()))


if __name__ == '__main__':
    main()
