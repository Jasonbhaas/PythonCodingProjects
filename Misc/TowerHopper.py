def is_hoppable(towers):
    i = 0
    while True:
        height = towers[i]
        if height == 0:
            return False
        elif height + i + 1 > len(towers):
            return True
        best_move = (float('-inf'), 0)
        for m in range(1, height + 1):
            delta_y = height - towers[i + m]
            if (m - delta_y) >= best_move[0]:
                best_move = (m - delta_y, m)
        i = best_move[1]


print(is_hoppable([4, 2, 0, 0, 2, 0]))
print(is_hoppable([4, 2, 0, 0, 2, 0, 0]))
print(is_hoppable([4, 10, 3, 2, 4, 0, 0, 0, 0, 0]))
