"""
Input: "123"
Output: 3
Explanation:
There are 3 possible valid & complete decodings:
1.) ["1", "2", "3"] =>["a", "b", "c"]
2.) ["12", "3"] => ["l", "c"]
3.) ["1", "23"] => ["a", "w"]
"""

letter_map = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z",
}

# letters = ' abcdefghijklmnopqrstuvwxyz'

master_output = []


def decode_ways(input: str, output: list = [], item_to_add=None):
    this_output = output.copy()

    if item_to_add:
        this_output.append(item_to_add)

    len_input = len(input)

    if not input:
        master_output.append(this_output)
        return

    if len_input > 1:
        combined_next = int(input[0:2])
        if combined_next <= 26:
            decode_ways(input[2:], this_output, letter_map[combined_next])

    decode_ways(input[1:], this_output, letter_map[int(input[0])])


decode_ways("123")  # -> 3
# decode_ways("33")  # -> 1
print(master_output)