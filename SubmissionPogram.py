import sys

class SudokuGame:
    def __init__(self):
        # Initialize the Sudoku grid as a 2D list (9x9)
        self.grid = [['.' for _ in range(9)] for _ in range(9)]
        self.gridpotential = [['.' for _ in range(9)] for _ in range(9)]
        self.round = 0
    
    def roundup(self):
        self.round += 1
    
    def update_grid(self, position):
        column = ord(position[0]) - 65
        row = ord(position[1]) - 97
        number = position[2]
        self.grid[column][row] = number
    
    def update_grid_potential(self, position):
        print('h')

    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))

# Create an instance of the SudokuGame class
game = SudokuGame()

# Main game loop
while True:
    command = input().strip()
    
    if command == "Start":
        # It's your turn as the First player
        # Implement the logic to make a move as the First player
        move = "Ab3!"  # Replace with your move logic
        print(move)
        sys.stdout.flush()
    elif command.startswith("Quit"):
        break
    elif command.startswith(""):  # Replace with proper move parsing
        # It's your turn as the Second player
        # Implement the logic to make a move as the Second player
        move = "Gh6"  # Replace with your move logic
        print(move)
        sys.stdout.flush()
    
    # Implement the logic to update the grid based on opponent's move
    game.update_grid(move)

    #Note the round we are in
    game.roundup()
    print(game.round)
    
    # Display the current state of the Sudoku grid
    game.display_grid()

# End of the game
