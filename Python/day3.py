import itertools


def spiralCoordinates():
    """
    Cheesy way to do this. There's a mathematical closed form-ish solution to this, but hacking it in place as a
    generator
    """

    directionFactors = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0),
    }

    directionOrder = ['R', 'U', 'L', 'D']

    x = y = 0
    currentDirection = 'R'
    stepPairSize = 1

    while True:
        for iteration in range(0, 2):
            xAxisMove, yAxisMove = directionFactors[currentDirection]

            for _ in range(0, stepPairSize):
                x += xAxisMove
                y += yAxisMove

                yield (x, y)

            currentDirection = directionOrder[(directionOrder.index(currentDirection) + 1) % len(directionOrder)]

        stepPairSize += 1


def cumulativeSpiralGenerator():
    """
    Slightly less cheesy. Use a dict to store coordinates we've already calculated, then just look up existing values
    we care about
    """

    grid = {
        (0, 0): 1
    }

    for xCoordinate, yCoordinate in spiralCoordinates():
        newValue = 0

        for xAdjustment in (-1, 0, 1):
            for yAdjustment in (-1, 0, 1):
                newValue += grid.get((xCoordinate + xAdjustment, yCoordinate + yAdjustment), 0)

        grid[(xCoordinate, yCoordinate)] = newValue

        yield newValue


def main():
    stepCount = 325489

    coordinates = list(itertools.islice(spiralCoordinates(), stepCount))[-2]

    print(coordinates)

    print(abs(coordinates[0]) + abs(coordinates[1]))

    for cumulativeValue in cumulativeSpiralGenerator():
        if cumulativeValue > stepCount:
            print(cumulativeValue)
            break


if __name__ == '__main__':
    main()
