class Grid:

    def __init__(self, size):
        self.size = size
        self.grid = [[0 for row in range(self.size)] for col in range(self.size)]

    def __repr__(self):
        
        print("\nCurrent state of the board: \n ")
        grid_repr = str()
        for row in self.grid:
            for char in row:
                grid_repr += str(char) + ','
            grid_repr += '\n'     
        return grid_repr
    
    def get_empy_cell_coordinates(self):
        for row in range(self.size):
            for column in range(self.size):
                if self.grid[row][column] == 0:
                    return row, column

    def grid_is_full(self):
        for row in range(self.size):
            for column in range(self.size):
                if self.grid[row][column] == 0:
                    return False
        
        return True
