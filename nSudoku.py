def box(n, i, j):
    r = i // (n**(1/2))
    c = j // (n**(1/2))

    return int((r * (n**(1/2))) + c)

def safe(x, n, r, c, b, i, j):
    if r[i][x - 1] == 1:
        return False
    elif c[j][x - 1] == 1:
        return False
    elif b[box(n, i, j)][x - 1] == 1:
        return False
    else:
        return True

def backtrack(curr, matrix, n, r, c, b, s, d):
    if curr >= len(s):
        return matrix
    print("s", s)
    print("curr", curr)
    print("d", d)

    i = s[curr][1]
    j = s[curr][2]
    print("i", i)  # logs
    print("j", j)

    for num in d[(i, j)]:
        print("checking ", num)
        if not safe(num, n, r, c, b, i, j):
            continue
        r[i][num - 1] = 1
        c[j][num - 1] = 1
        b[box(n, i, j)][num - 1] = 1

        if backtrack(curr + 1, matrix, n, r, c, b, s, d):
            matrix[i][j] = num
            return matrix
        r[i][num - 1] = 0
        c[j][num - 1] = 0
        b[box(n, i, j)][num - 1] = 0
    return False

def solve(sudoku, n=9):
    r = [[0 for _ in range(n)] for _ in range(n)]
    c = [[0 for _ in range(n)] for _ in range(n)]
    b = [[0 for _ in range(n)] for _ in range(n)]
    d = {}  # dictionary to store possible numbers for each empty cell
    s = []

    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            x = sudoku[i][j]
            if x == 0:
                d[(i, j)] = []
                print(d)  # temporary log
            else:
                r[i][x - 1] = 1
                c[j][x - 1] = 1
                b[box(n, i, j)][x - 1] = 1

    for (i, j) in d.keys():
        temp = []
        for num in range(1, n+1):
            if safe(num, n, r, c, b, i, j):
                temp.append(num)
        d[(i, j)] = temp
        s.append([len(temp), i, j])

    s = sorted(s)  # sort the list of empty cells by the number of possibilities
    return backtrack(0, sudoku, n, r, c, b, s, d)

def test():
    grid = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    solved_grid = solve(grid)
    if solved_grid:
        for row in solved_grid:
            print(row)
    else:
        print("not solvable")

def nSolve():
    n = int(input("Enter the value of n (must be a perfect square): "))
    root_n = int(n**0.5)
    if root_n * root_n != n:
        print("n must be a perfect square (e.g., 4, 9, 16, etc.).")
        return

    print(f"Enter the Sudoku puzzle of size {n}x{n}, row by row, with 0 for empty cells:")
    sudoku = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        if len(row) != n:
            print(f"Each row must contain exactly {n} numbers.")
            return
        sudoku.append(row)

    solved_grid = solve(sudoku, n)
    if solved_grid:
        print("Solved Sudoku:")
        for row in solved_grid:
            print(" ".join(map(str, row)))
    else:
        print("Not solvable")

if __name__=="__main__":
    nSolve()

