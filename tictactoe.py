
winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])


def available_moves(board):
    moves = []

    for i in range(9):
        if board[i] == " ":
            moves.append(i)

    return moves


def check_winner(board):
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None

def evaluate(board):
    winner = check_winner(board)

    if winner == "O":
        return 1

    if winner == "X":
        return -1

    return 0

def minimax(board, maximizing):
    score = evaluate(board)

    if score != 0:
        return score

    if not available_moves(board):
        return 0

    if maximizing:
        best_score = -float("inf")

        for move in available_moves(board):
            board[move] = "O"

            score = minimax(board, False)

            board[move] = " "

            best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for move in available_moves(board):
            board[move] = "X"

            score = minimax(board, True)

            board[move] = " "

            best_score = min(best_score, score)

        return best_score


def human_move(board):
    while True:
        move = input("Enter your move (0-8): ")

        if move.isdigit():
            move = int(move)

            if move in available_moves(board):
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")
        else:
            print("Please enter a number between 0 and 8.")


def machine_move(board):
    best_score = -float("inf")
    best_move = None

    for move in available_moves(board):
        board[move] = "O"

        score = minimax(board, False)

        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    board[best_move] = "O"


def play_game():
    board = [
        " ", " ", " ",
        " ", " ", " ",
        " ", " ", " "
    ]

    while True:

        # Human turn
        print_board(board)
        human_move(board)

        winner = check_winner(board)

        if winner:
            print_board(board)
            print("Winner:", winner)
            break

        # Draw check
        if not available_moves(board):
            print_board(board)
            print("Draw!")
            break

        # Machine turn
        machine_move(board)

        winner = check_winner(board)

        if winner:
            print_board(board)
            print("Winner:", winner)
            break

        # Draw check
        if not available_moves(board):
            print_board(board)
            print("Draw!")
            break




play_game()