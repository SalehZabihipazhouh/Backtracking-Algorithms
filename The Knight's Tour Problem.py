board_size = 6
moves = [(1,2), (2,1), (1,-2), (-2,1), (-1,-2), (-2,-1), (-1,2), (2,-1)]
def is_valid_move(x,y,board):   # This function return True if we have valid move in x , y location
    return 0 <= x < board_size and 0 <= y < board_size and board[x][y] == -1

def print_board(board):  # This function make matrix of the board with the count move in every square
    for row in board:
        print(" ".join(f"{cell:2d}" for cell in row))

def solve_problem(x, y, move_count, board): # This function check the problem is solved or not and help to solve problem
    board[x][y] = move_count
    if move_count == board_size * board_size:
        print("The solution is :")
        print_board(board)
        return True
    for dx, dy in moves:
        x_move, y_move = x + dx, y + dy
        if is_valid_move(x_move, y_move, board):
            if solve_problem(x_move, y_move,move_count + 1, board):  # Here call again the function and here use backtracking algorithm
                return True
    board[x][y] = -1
    return False

def knight_tour(start_x = 0, start_y= 0):  # With this function we start to solve problem
    board = [[-1 for _ in range(board_size)] for _ in range(board_size)]

    if not solve_problem(start_x, start_y, 1, board):
        print("No solution")

if __name__ == "__main__":
    knight_tour(0, 0)  # Call the function to solve problem
