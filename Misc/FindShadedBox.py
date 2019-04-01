import collections


def find_shaded_box(box):
    Coordinate = collections.namedtuple('Coordinate', ['x', 'y'])
    height = len(box)
    width = len(box[0])

    def check_center(l, r, b, t):
        return box[(t + b) // 2][(l + r) // 2] == 1

    def explore_box():
        i = 0
        while (2 ** (i - 1) < max(width, height)):
            divisor = 2 ** i
            for j in range(divisor):
                left = (width * j) // divisor
                right = (width * (j + 1)) // divisor - 1
                for k in range(divisor):
                    bottom = (height * k) // divisor
                    top = (height * (k + 1)) // divisor - 1
                    if (right >= 0 and top >= 0):
                        if check_center(left, right, bottom, top):
                            return Coordinate(x=(left + right) // 2, y=(top + bottom) // 2)
            i += 1

    coor = explore_box()

    left = coor.x
    while left - 1 >= 0 and box[coor.y][left - 1] == 1:
        left -= 1

    right = coor.x
    while right + 1 < width and box[coor.y][right + 1] == 1:
        right += 1

    top = coor.y
    while top - 1 >= 0 and box[top - 1][coor.x] == 1:
        top -= 1

    bottom = coor.y
    while bottom + 1 < height and box[bottom + 1][coor.x] == 1:
        bottom += 1

    return (left, right, top, bottom)


mybox = [[0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 0, 0],
         [0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]

print(find_shaded_box(mybox))
