class Grid:

    def __init__(self, size):
        self.grid = [[0 for row in range(size)] for col in range(size)]
    
    def __repr__(self):
        print("\n Current state of the board: \n")
        board_repr_string = (str(row) for row in self.grid)
        print(board_repr_string)

    def get_empy_cell(self):
        for x in range(self.size):
            for y in range(self.size):
                if grid[x][y] == 0:
                    return x, y
        else:
            return None
    
    def grid_is_filled(self):
        for x in range(9):
            for y in range(9):
                if grid[x][y] == 0:
                    return False
        else:
            return True





