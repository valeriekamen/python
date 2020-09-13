def remove_one(num):
    print('num',num)
    if num > 2:
        print(num - 1)
        remove_one(num-1)
    print(num, num - 1)
    return num - 1

remove_one(4)