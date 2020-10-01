"""
Input:
[
  ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
  ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
  ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
  ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
  ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
  ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
  ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
  ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
  ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

Output:
[
  ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
  ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
  ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
  ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
  ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
  ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
  ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
  ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
  ['3', '4', '5', '2', '8', '6', '1', '7', '9']
]
"""


def remove_from_possibilities(possibilities: list, item: str) -> list:
    if item in possibilities:
        possibilities.remove(item)

    return possibilities


def get_square_start(index: int) -> int:
    start = 0
    if 3 <= index <= 5:
        start = 3
    if 6 <= index <= 8:
        start = 6
    return start


def build_square(i: int, j: int, input: list) -> list:
    this_square = []
    range_i = get_square_start(i)
    range_j = get_square_start(j)

    for n in range(range_i, range_i + 3):
        for u in range(range_j, range_j + 3):
            this_square.append(input[n][u])

    return this_square


def solve_sodoku(input: list, iteration=0) -> list:
    iteration += 1
    unsolved_squares = 0
    for i in range(0, 9):
        for j in range(0, 9):
            possibilities = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

            this_cell = input[i][j]
            if not this_cell == ".":
                continue

            this_row = input[i]
            this_col = [input[n][j] for n in range(0, 9)]
            this_square = build_square(i, j, input)

            all_to_eliminate = this_row + this_col + this_square

            for item in all_to_eliminate:
                remove_from_possibilities(possibilities, item)

            if len(possibilities) == 1:
                input[i][j] = possibilities[0]
                print("ADDING", possibilities[0])
                continue

            unsolved_squares += 1

    if unsolved_squares:
        solve_sodoku(input, iteration)

    print("Finished iteration {}".format(iteration))
    return input


input = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
assert solve_sodoku(input) == [
    ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
]
