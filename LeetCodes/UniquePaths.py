def uniquePaths(m: int, n: int) -> int:
    paths = 0

    def DFS(row, col):
        if row >= n or col >= m:
            return
        else:
            if row == n-1 and col == m-1:
                nonlocal paths
                paths += 1
                return
            else:
                # explore to right
                DFS(row, col+1)
                # explore down
                DFS(row + 1, col)

    DFS(0, 0)
    return paths


print(uniquePaths(7, 3))
