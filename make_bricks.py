def make_bricks(small: int, big: int, goal: int) -> bool:
    total_bricks = small + (big * 5)
    if total_bricks < goal:
        return False

    needed_small = goal % 5
    if needed_small > small:
        return False

    return True


assert not make_bricks(1, 5, 2)
assert make_bricks(10, 1, 8)
assert make_bricks(3, 1, 8)
assert not make_bricks(3, 1, 9)
assert make_bricks(3, 2, 10)
assert make_bricks(12, 1, 15)
