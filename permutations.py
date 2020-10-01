"""
Given a collection of distinct integers, return all possible permutations.

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
output = []


def make_permutations(input: list, new_list: list = [], index=0) -> list:
    print("IN", input, new_list)
    ni = input.copy()
    nn = new_list.copy()
    if not input:
        output.append(new_list)
        print(output)
        return

    p = input.pop(index)
    for i in range(len(input)):
        print(i)

    # # ip = input.copy()
    # # new = new_list.copy()

    # p = input.pop(0)
    # new_list.append(p)
    # for i in input:
    #     input.remove(i)
    #     new = new_list.copy()
    #     new.append(i)
    #     make_permutations(input, new)
    #     # for i in input:

    #     #     o = ip.pop(0)
    #     #     new.append(o)
    #     #     make_permutations(ip, new)


make_permutations(input=[1, 2, 3])
