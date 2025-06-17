def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw(board):
    return all(cell != " " for cell in board)

def play_game():
    board = [" "] * 9
    current_player = "X"
    
    print("🎲 Welcome to Tic-Tac-Toe!")
    print("Player 1 is X, Player 2 is O")
    print("Positions are numbered 1-9 like this:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    
    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        except ValueError:
            print("⚠️ Invalid input. Enter a number 1-9.")
            continue

        if move < 0 or move > 8:
            print("⚠️ Move out of range. Pick between 1 and 9.")
            continue
        if board[move] != " ":
            print("⚠️ That spot is already taken.")
            continue
        
        board[move] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print(f"🏆 Player {current_player} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
