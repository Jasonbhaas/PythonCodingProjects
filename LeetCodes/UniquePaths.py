def uniquePaths(m: int, n: int) -> int:
    paths_from = [[1] * m for _ in range(n)]

    for row in range(n-2, -1, -1):
        for col in range(m - 2, -1, -1):
            paths_from[row][col] = paths_from[row + 1][col] + \
                paths_from[row][col + 1]

    return paths_from[0][0]


print(uniquePaths(7, 3))
