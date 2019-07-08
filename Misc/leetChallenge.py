def prisonAfterNDays(cells, N):
    already_seen = []
    j = 0
    while j < N:
        j += 1
        temp = [0] * 8
        for i in range(1, 7):
            temp[i] = (cells[i-1] + cells[i+1]) % 2
        cells = temp
        if cells in already_seen:
            break
        already_seen.append(cells)
    if j < N:
        loop_start = cells
        loop_counter = 0
        while True:
            loop_counter += 1
            temp = [0] * 8
            for i in range(1, 7):
                temp[i] = (cells[i-1] + cells[i+1]) % 2
            cells = temp
            if cells == loop_start:
                print(loop_counter)
                break

        remainder = (N - j) % loop_counter
        k = 0
        while k < remainder:
            k += 1
            temp = [0] * 8
            for i in range(1, 7):
                temp[i] = (cells[i-1] + cells[i+1]) % 2
            cells = temp

    return cells


def old_way(cells, N):
    j = 0
    while j < N:
        j += 1
        temp = [0] * 8
        for i in range(1, 7):
            temp[i] = (cells[i-1] + cells[i+1]) % 2
        cells = temp
    return cells


def nextday(cells):
    return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1])
            for i in xrange(8)]


def prisonAfterNDays(self, cells, N):
    seen = {}
    while N > 0:
        c = tuple(cells)
        if c in seen:
            N %= seen[c] - N
        seen[c] = N

        if N >= 1:
            N -= 1
            cells = nextday(cells)

    return cells


cells = [0, 1, 0, 0, 1, 1, 1, 0]
N = 1000000000


#temp = prisonAfterNDays(cells, 100)
print(prisonAfterNDays(cells, 1000))
#print(prisonAfterNDays(cells, 86))
print(old_way(cells, 1000))
