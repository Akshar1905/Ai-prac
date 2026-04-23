##Develop a program to solve the 8-Queens problem using backtracking or heuristic approaches.

N = 8

def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")


def is_safe(board, row, col):
    
    for i in range(row):
        if board[i][col] == 1:
            return False

    
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_queens(board, row):
    
    if row == N:
        print_solution(board)
        return True   

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_queens(board, row + 1):
                return True

            
            board[row][col] = 0

    return False



board = [[0 for _ in range(N)] for _ in range(N)]

if not solve_queens(board, 0):
    print("No solution exists")


###🔹 Aim
To solve the 8-Queens problem using backtracking.
🔹 Theory
The 8-Queens problem is a constraint satisfaction problem where 8 queens must be placed on a chessboard such that no two queens attack each other.
Conditions:
No same row
No same column
No diagonal attack
Backtracking is used to try all possible positions and undo incorrect choices.
🔹 Algorithm
Place queen row by row
Check if position is safe
If safe → place queen
Else → backtrack
Repeat until solution found
🔹 Explanation of Code
is_safe() checks column and diagonal conflicts
solve_queens() places queens recursively
If conflict occurs, it removes queen (backtracking)
Final board is printed
🔹 Conclusion
Backtracking efficiently solves constraint problems by eliminating invalid solutions early.
