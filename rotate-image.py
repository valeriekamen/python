# Rotate a square matrix clockwise one rotation
import math


def get_new_position(start_i, start_j, lim):
    # [0,0] -> [0,2]
    # print(start_j, lim - start_i)
    return start_j, lim - start_i


def rotate_image(input_matrix, number_times=None, start_i=0, start_j=0):
    print(input_matrix, number_times, start_i, start_j)

    lim = len(input_matrix)
    if number_times == 0:
        return input_matrix

    if not number_times:
        number_times = lim - 1

    print(number_times)
    # check if actually a square
    for side in input_matrix:
        if not len(side) == lim:
            return False
    starting_i = start_i
    starting_j = start_j

    # moving_i = start_i
    # moving_j = start_j

    # moving_val = input_matrix[moving_i][moving_j]

    for n in range(number_times):
        moving_i = start_i
        moving_j = start_j

        moving_val = input_matrix[moving_i][moving_j]
        for n in range(0, 4):

            print("moving", moving_val)
            new_i, new_j = get_new_position(moving_i, moving_j, lim - 1)
            next_moving_val = input_matrix[new_i][new_j]

            input_matrix[new_i][new_j] = moving_val
            moving_val = next_moving_val
            moving_i = new_i
            moving_j = new_j
        start_j += 1

    rotate_image(
        input_matrix, math.floor(number_times / 2), starting_i + 1, starting_j + 1
    )

    print(input_matrix)
    return input_matrix


assert rotate_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
]
assert rotate_image(
    [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
) == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
assert rotate_image([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
assert rotate_image([[1]]) == [[1]]


"""
Works, maybe overly complicated

def rotate_image(input_matrix):
    lim = len(input_matrix)
    # check if actually a square
    for side in input_matrix:
        if not len(side) == lim:
            return False

    # list of proper length in order of final positions
    new_nums = [None] * (lim ** 2)
    
    for i in range(lim): # inside matrix
        for j in range(lim):  # inside row            
            num = input_matrix[i][j]
            # new position in matrix is [(lim - 1) - j][i]
            # ex: [0][0] moves to [0][2]
            new_j = (lim - 1) - i

            # new index in grand scheme is 3 * i + j
            # ex: [0][2] is 3rd in list of 9 numbers, 3 * 0 + 2 as index 2
            new_pos = (lim * j) + new_j
            new_nums[new_pos] = num


    # go through matrix and replace what has been calculated in new_nums
    for i in range(lim): # inside matrix
        for j in range(lim):  # inside row
            this_pos = (lim * i) + j
            input_matrix[i][j] = new_nums[this_pos]

    return input_matrix




Creates new matrix, does not change in place

def rotate_image(input_matrix):
    # check if actually a square
    for side in input_matrix:
        if not len(side) == len(input_matrix):
            return False

    new_matrix = []
    for i in range(len(input_matrix)):
        new_row = []
        for side in input_matrix:
            new_row.append(side[i])
        new_row.reverse()
        new_matrix.append(new_row)

    return new_matrix
"""