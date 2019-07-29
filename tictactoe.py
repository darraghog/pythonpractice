# Tic-Tac-Toe Game
#

import argparse
        
# Return winner of game
# 1 = Player 1
# 2 = Player 2
# 0 = Draw
player_dict = {1 : "X", 2 : "O", 0 : " "}

def init_grid(number_columns):
    grid = []
    for row in range(number_columns):
        grid.append([]) # add bew row
        for col in range(number_columns):
            grid[row].append(0) # add columns to row
    return grid


# Given a player number, updates grid with players move
# Returns rol, col of move
def input_move(player, grid):
    number_columns = len(grid[0])
    valid = False
    while not valid:
        try:
            coords = input("Player "+ str(player) + " - enter row, col: ")
        except  EOFError:
            exit(0)
        if not coords or len(coords) == 0:
            exit(0)
        try: 
            (row, col) = map(int, coords.split(","))
        except  ValueError:
            print("Must be in form x,y where x and y > 0 and < %s" % str(number_columns))   
            continue   
        valid = (row > 0 and row <= number_columns) and (col > 0 and col <= number_columns) and (grid[row-1][col-1] == 0)
    grid[row-1][col-1] = player
    return (row-1,col-1)


# Return winner
# winner = 1->Player 1, 2->Player 2, 0->No winner (game not finished) or draw
def check_winner(grid):
    number_columns = len(grid[0])

       # Check columns
    #print("Phase 1")
    for col in range(number_columns):
        first = grid[0][col]
        match = True
        row = 0
        while row < number_columns and match:
             match = (first == grid[row][col])
             row += 1

        if match and first:
            return first

    #print("Phase 2")
    # Check rows
    for row in range(number_columns):
        first = grid[row][0]
        match = True
        col = 0
        while col < number_columns and match:
            match = (first == grid[row][col])
            col += 1

        if match and first:
            return first

    #print("Phase 3")    
    # Check diagonals - left-to-right
    first = grid[0][0]
    match = True
    i = 0
    while i < number_columns and match:
        match = (first == grid[i][i])
        i += 1

    if match and first:
        return first

    #print("Phase 4")
    # Check diagonals - right-to-left
    first = grid[number_columns-1][number_columns-1]
    match = True
    i = number_columns-1
    while i > 0 and match:
        #print("grid[-1-%d][%d]=%s" % (i, i, grid[-1-i][i]))
        match = (first == grid[i][i])
        i -= 1

    if match and first:
        return first

    # No winner
    return 0

# Print a grid structure, given a nxn dimensional array
def print_board(grid):
    width = len(grid[0]) # number of entries in a tuple
    height = len(grid) # number of tuples

    # First print top
    for iw in range(width):
        print(" ---", end='')

    print("")

    for ih in range(height):
        for iw in range(width):
            #print("| %d " % grid[ih][iw], end='')
            print("| %s " % player_dict[grid[ih][iw]], end='')
        print("|")
    
        # Line break
        for iw in range(width):
            print(" ---",end='')
        print("")
        

    print("")


# 
# Handle input and results for a new game. 
# 
# Inputs: game board, name of game, number of moves left
#
# Returns 0,1,2 for draw, player 1 winner, player 2 winner
#
# Designed to handle test scenarios (or incomplete games)
def process_game(game, title, moves_left):
    print ("%s\n%s\n%s" % (str('*' * 15), title, str('*' * 15)))
    player = 0 # start with player 1
    winner = check_winner(game)  # may be given pre-filled board
    print_board(game)
    while moves_left and winner == 0:
        (row, col) = input_move(player+1, game)
        print_board(game)
        player = (player + 1) % 2
        moves_left -= 1  

        winner = check_winner(game)

    if winner:
        print("Player %d wins!" % winner)
    else:
        print("Draw!!\n")

    print(str('=' * 15))
    return winner 


# Check logic
def run_tests():

    # Game:
    #  "game" : list of lists
    #  "title" : string
    #  "winner" : integer (0 = draw, 1 = player 1, 2 = player 2)
    game_list = []

    winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

    game_list.append({'game' : winner_is_2, 'title' : "Winner is 2", 'winner' : 2})

    winner_is_1 = [[1, 2, 0],[2, 1, 0],[2, 1, 1]]
    game_list.append({"game" : winner_is_1, "title" : "Winner is 1", "winner" : 1})

    winner_is_also_1 = [[0, 1, 0],
        [2, 1, 0],
        [2, 1, 1]]
    game_list.append({"game" : winner_is_also_1, "title" : "Winner is also 1",  "winner" : 1})

    no_winner = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 2]]

    game_list.append({"game" : no_winner, "title" : "No Winner", "winner" :0})


    also_no_winner = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 0]]

    game_list.append({"game" : also_no_winner, "title" : "Also No Winner", "winner" : 0})


    for idx in range(len(game_list)):
        board = game_list[idx]
        winner = process_game(board['game'],board['title'], 0)  # No moves left
        if (winner != board['winner']):
            print("** TEST FAILED: %s: %d != %d" % (board['title'], winner, board['winner']))
        else:
            print("** TEST SUCCEEDED: %s" % board['title'])





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tic Tac Toe.')
    parser.add_argument("--tests",action='store_const',const=1,help="run tests")

    args = parser.parse_args()

    if args.tests:
        run_tests()
        exit(0)

    grid = init_grid(3) 
    process_game(grid,"User Game", len(grid[0])*len(grid[0]))


