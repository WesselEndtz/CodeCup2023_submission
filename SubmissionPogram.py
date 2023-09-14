import sys
import random


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
    
    def get_box_number(self, num):
        colum_min = int(num/3)*3
        row_min = num-3*int(num/3)
        box = []
        for column in sudoku_grid[colum_min:colum_min+3]:
            box.append(column[row_min:row_min+3])
        return box

    
    def Simple_Move(self):
        random_number = random.randint(1, 9)
        column_num = 0
        for column in self.grid:
            if random_number not in column:
                column = column_num
                row_num = 0
                for row in list(map(list, zip(*self.grid))):
                    if random_number not in row:
                        row = row_num
                        box = 
                        print(box)
                row_num += 1
        column_num += 1
        
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
