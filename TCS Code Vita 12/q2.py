DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def valid_move(r, c, M, N, grid):
    return 0 <= r < M and 0 <= c < N and grid[r][c] != 'H'

def bfs(M, N, grid, start, target):
    queue = [(start, 0)]
    visited = {start}

    while queue:
        (r1, c1, r2, c2), steps = queue.pop(0)

        if (r1, c1) == target or (r2, c2) == target:
            return steps

        for dr, dc in DIRECTIONS:
            nr1, nc1 = r1 + dr, c1 + dc
            nr2, nc2 = r2 + dr, c2 + dc
            if valid_move(nr1, nc1, M, N, grid) and valid_move(nr2, nc2, M, N, grid):
                new_state = (nr1, nc1, nr2, nc2)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))

        if r1 == r2:
            if r1 + 1 < M and valid_move(r1+1, c1, M, N, grid) and valid_move(r1+1, c2, M, N, grid):
                new_state = (r1, c1, r1+1, c1)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
        elif c1 == c2:
            if c1 + 1 < N and valid_move(r1, c1+1, M, N, grid) and valid_move(r2, c1+1, M, N, grid):
                new_state = (r1, c1, r1, c1+1)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))

    return "Impossible"

def solve_sofa_problem(M, N, grid):
    start, target = None, None
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 's':
                if valid_move(i+1, j, M, N, grid) and grid[i+1][j] == 's':
                    start = (i, j, i+1, j)
                elif valid_move(i, j+1, M, N, grid) and grid[i][j+1] == 's':
                    start = (i, j, i, j+1)
            elif grid[i][j] == 'S':
                target = (i, j)

    return "Impossible" if not start or not target else bfs(M, N, grid, start, target)

M, N = 5, 5
grid1 = [
    ['s', 's', '0', '0', '0'],
    ['0', 'H', '0', '0', 'H'],
    ['0', 'H', '0', 'H', 'H'],
    ['0', 'H', '0', '0', 'H'],
    ['0', '0', '0', 'S', 'S']
]
print(solve_sofa_problem(M, N, grid1))

grid2 = [
    ['s', 's', '0', 'H', '0'],
    ['0', 'H', '0', '0', 'H'],
    ['0', 'H', '0', 'H', 'H'],
    ['0', 'H', '0', '0', 'H'],
    ['0', '0', '0', 'S', 'S']
]
print(solve_sofa_problem(M, N, grid2))
