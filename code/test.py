import numpy
m = 3
n = 3
walls = [(0, 2), (1, 1), (2, 2)]
start = (2, 1)
goal = (0, 1)


def testingMatrix(m, n, walls):
    init_matrix = numpy.zeros([m, n])
    # i = 0

    for i in walls:
        init_matrix[walls(i)] = 1
        # i = i+1
    # print init_matrix
        # print i
    return init_matrix


# for (x,y) in walls:
#     init_matrix(x,y) = 1
testingMatrix(m, n, walls)


# for x in array:

# for (x = 0; x < len(array); i+)
