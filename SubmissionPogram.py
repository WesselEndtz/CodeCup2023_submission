import sys
import random
import copy

class SudokuGame:
    def __init__(self):
        # Initialize the Sudoku grid as a 2D list (9x9)
        self.grid = [['.' for _ in range(9)] for _ in range(9)]
        self.gridpotential = [['.' for _ in range(9)] for _ in range(9)]
        self.round = 0
    
    def roundup(self):
        self.round += 1
    
    def update_grid(self, position, raw=False):
        print(position)
        if raw == False:
            column = ord(position[0]) - 65
            row = ord(position[1]) - 97
        else:
            column = int(position[0])
            row = int(position[1])
        number = position[2]
        self.grid[column][row] = number
    
    def get_box_of_number(self, num):
        row_min = int(num/3)*3
        colum_min = (num-3*int(num/3))*3
        box = []
        for column in self.grid[row_min:row_min+3]:
            box.append(column[colum_min:colum_min+3])
        return box

    
    def Simple_Move(self):
        """
        strategy is to generate a random number and find the first place that 
        the random number checks all boxes (not in the row, column and box)
        """
        random_number = random.randint(1, 9)
        row_num = 0
        Imagined_grid = copy.deepcopy(self.grid)
        Reverse_imagined_grid = list(map(list, zip(*Imagined_grid)))
        print('random_num = ', random_number)
        # for each row in the grid
        for row in Imagined_grid:
            # while to keep iterating until "." locations are exhauset
            # check if the random number is in the row
            if str(random_number) not in str(row):
                print('empty row num', row_num, 'row = ', row)
                try: 
                    openlocation = row.index(".")
                    Imagined_grid[row_num][openlocation] = "-"
                    print('new grid imagine = ', Imagined_grid, 'openlocation = ', openlocation)
                except ValueError:
                    print('no open locations on row')
                    row_num += 1
                    continue  # Skip the current iteration of the loop
                # when finding the row we set that as the row to check
                row = row_num
                if str(random_number) not in str(Reverse_imagined_grid[openlocation]):
                    # find the box_number our current position is in 0-8
                    box_num = int(row_num/3)*3+int(openlocation/3)
                    # Get the box of the specific box number
                    box = self.get_box_of_number(box_num)
                    print("box_num =", box_num)
                    if str(random_number) not in str(box):
                        self.update_grid(str(row_num) + str(openlocation) + str(random_number), raw=True)
                        print('found position', row_num, openlocation, random_number)
                        return "Ff2"
            row_num += 1
        
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
        move = game.Simple_Move()  # Replace with your move logic
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
