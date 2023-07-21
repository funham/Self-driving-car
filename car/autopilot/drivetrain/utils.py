def sign(x):
    return (x > 0) - (x < 0)


def clip(x, x_min, x_max):
    return min(max(x_min, x), x_max)


class LRPair:
    def __init__(self, left, right):
        self.left = left
        self.right = right
