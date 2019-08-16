from pprint import pprint


def FindHamiltonianPaths(n):
    visited = [[False] * n for _ in range(n)]

    directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # right, down, left, up

    results = []
    length = n * n

    def AddResult(path):
        path = list(map(lambda coor: f'[{coor[0]},{coor[1]}]->', path))
        path_str = "".join(path)
        path_str = path_str[:-2]
        results.append(path_str)

    def DFS(row, col, path):
        if (row < 0 or row >= n or col < 0 or col >= n or visited[row][col]):
            return
        else:
            path.append([row, col])
            if len(path) == length:
                AddResult(path)
                path.pop()
                return
            else:
                visited[row][col] = True
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    DFS(new_row, new_col, path)
                visited[row][col] = False
                path.pop()

    DFS(0, 0, [])

    pprint(results)


FindHamiltonianPaths(3)
