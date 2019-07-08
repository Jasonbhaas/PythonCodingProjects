def nextDay(cells):
    temp = [0] * 8
    for i in range(1, 7):
        temp[i] = (1 + cells[i-1] + cells[i+1]) % 2
    return temp


def nextDayOther(cells):
    return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1])
            for i in range(8)]


def prisonAfterNDas(cells, N):
    already_seen = {}  # Key= prison cells config, value = N - kth day
    while N > 0:
        if tuple(cells) in already_seen:
            loop_length = already_seen[tuple(cells)] - N
            N = N % loop_length
        else:
            already_seen[tuple(cells)] = N
        if N > 0:
            cells = nextDay(cells)
        N -= 1

    return cells


cells = [1, 0, 0, 1, 0, 0, 1, 0]

last1 = [1, 0, 0, 1, 0, 0, 1, 0]
last2 = [1, 0, 0, 1, 0, 0, 1, 0]
for i in range(5):
    last1 = nextDay(last1)
    last2 = nextDayOther(last2)
    print(last1)
    print(last2)
    print(" ")
