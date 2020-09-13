

def asteroid_collisions(asteriods):
    output = []
    for current_num in asteriods:
        if current_num > 0:
            output.append(current_num)

        else:
            for n in output[::-1]:
                if n < 0:
                    output.append(current_num)
                    break

                if abs(current_num) > n:
                    output.pop()
                else:
                    break
            if len(output) == 0:
                output.append(current_num)
    print(output)
    return output


assert asteroid_collisions([2, 5, -10]) == [-10]
assert asteroid_collisions([2, 3, 1, 10, -5]) == [2, 3, 1, 10]
assert asteroid_collisions([-3, -2, 10, 5]) == [-3, -2, 10, 5]
assert asteroid_collisions([-1, 10, -20]) == [-1, -20]
