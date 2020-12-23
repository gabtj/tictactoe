from typing import List      

def check_winner(grid: List[list]):
    """ 
    Checks to see if there is a winner based on the current state of the grid.
    >>> game_grid = [['X', 'X', 'X'], ['.', '.', '.'], ['.', '.', '.']]
    >>> check_winner(game_grid)
    0
    
    >>> game_grid = [['O', '.', '.'], ['.', 'O', '.'], ['.', '.', 'O']]
    >>> check_winner(game_grid)
    1
    
    >>> game_grid = [['X', 'O', 'X'], ['.', '.', '.'], ['.', '.', '.']]
    >>> check_winner(game_grid)
    -1
    """
    letter_count = 0
    
    i = 0
    j = 0
    
    # Rows for X and O
    for i in range(3):
        x_count = 0
        o_count = 0
        for j in range(3):
            if grid[i][j] == "X":
                x_count += 1
            if grid[i][j] == "O":
                o_count += 1 
            
            if x_count == 3:
                return 0
            
            if o_count == 3:
                return 1
    
    # Columns for X and O
    for j in range(3):
        x_count = 0
        o_count = 0
        for i in range(3):
            if grid[i][j] == "X":
                x_count += 1
            if grid[i][j] == "O":
                o_count += 1         
    
            if x_count == 3:
                return 0
            
            if o_count == 3:
                return 1
    
    # Diagonal X
    if grid[0][0] == "X" and grid[1][1] == "X"  and grid[2][2] == "X" :
        return 0
    
    if grid[0][2] == "X"  and grid[1][1] == "X" and grid[2][0] == "X":
        return 0

    # Diagonal O
    if grid[0][0] == "O" and grid[1][1] == "O"  and grid[2][2] == "O" :
        return 1
    
    if grid[0][2] == "O"  and grid[1][1] == "O" and grid[2][0] == "O":
        return 1
    
    # No winner
    return -1


def create_grid():
    """ Creates an empty grid.
    """
    return [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]


def display_grid(grid: List[list]):
    """ Displays grid with row and column numbers for two_player_game.
    """
    print('\n' + '  0 1 2')
    i = 0    
    for row in grid:
        printed_row = str(i)
        for item in row:
            printed_row = printed_row + " " + item
        print(printed_row.strip())
        i += 1
    print('\n')


def make_move(row, col, grid, marker):
    """
    Makes move, placing marker at row, col of grid.
    
    >>> game_grid = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    >>> make_move(0, 0, game_grid, 'X')
    >>> game_grid
    [['X', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    
    >>> game_grid = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    >>> make_move(0, 0, game_grid, 'O')
    >>> game_grid
    [['O', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    """    
    
    valid_move = False
    
    if grid[row][col] == ".":
        grid[row][col] = marker
        valid_move = True

    elif valid_move == False:
        while valid_move == False:
            print("Invalid move!")
            row = input("Please enter a row: ")
            while row not in ['0', '1', '2']:
                print('Invalid row!')
                row = input("Please enter a row: ")
            row = int(row)
            
            col = input("Please enter a col: ")
            while col not in ['0', '1', '2']:
                print('Invalid col!')
                col = input("Please enter a col: ")
            col = int(col)
            if grid[row][col] == ".":
                grid[row][col] = marker
                valid_move = True     

    
def play_turn(grid: List[list], moves_made: int, player: str):
    """ Initializes player turn.
    """

    if player == "one":
        marker = "X"
    else:
        marker = "O"

    print("Player", player, "turn")
    row = input("Please enter a row: ")
    while row not in ['0', '1', '2']:
        print('Invalid row!')
        row = input("Please enter a row: ")
    row = int(row)
    
    col = input("Please enter a col: ")
    while col not in ['0', '1', '2']:
        print('Invalid col!')
        col = input("Please enter a col: ")
    col = int(col)
    
    make_move(row, col, grid, marker)  
    moves_made += 1
    display_grid(grid)
    print("Moves made: " + str(moves_made))       
        	

def two_player_game():
    """
    Starts a two player game of TicTacToe.
    """
    grid = create_grid()
    display_grid(grid)

    moves_made = 0
    while moves_made < 9:
        play_turn(grid, moves_made, "one")
        moves_made += 1
        if check_winner(grid) is 0:
            print("Player one wins!" + "\n")
            return
        
        if moves_made == 9 and check_winner(grid) is -1:
            print("Tie game!")
            return
        
        play_turn(grid, moves_made, "two")
        if check_winner(grid) is 1:
            print("Player two wins!" + "\n")
            return  
        moves_made += 1


if __name__ == "__main__":

    playing = True
    
    while playing is True:
        two_player_game()
        play_again = input("Would you like to play again? Y/N: ")
        while play_again not in "YN":
            play_again = input("Would you like to play again? Y/N: ")         
        if play_again is "N":
            playing = False
            print("Thank you for playing.")
            break
        elif play_again is "Y":
            continue