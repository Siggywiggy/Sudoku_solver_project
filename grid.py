class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for row in range(self.size)] for col in range(self.size)]

    def __repr__(self):

        print("\nCurrent state of the board: \n ")
        grid_repr = str()
        for row in self.grid:
            for char in row:
                grid_repr += str(char) + " "
            grid_repr += "\n"
        return grid_repr

    # Insert a value to given coordinates - row = grid[x], column = grid[x][y]

    def insert(self, value, row, column):
        self.grid[row][column] = value

    # Get first empty cell coordinates (row and column) in a grid

    def get_empy_cell_coordinates(self):
        for row in range(self.size):
            for column in range(self.size):
                if self.grid[row][column] == 0:
                    return row, column
        return False

    # Check if grid has a single empty/blank cell (value 0)

    def grid_is_full(self):
        is_full = True
        for row in range(self.size):
            for column in range(self.size):
                if self.grid[row][column] == 0:
                    is_full = False
                    break
        return is_full

    # Check if value exists in a given row (sublist index)

    def value_in_row(self, value, row):
        for y_index in range(self.size):
            if self.grid[row][y_index] == value:
                return True
        return False

    # Check if value exists in given column

    def value_in_column(self, value, column):
        for x_index in range(self.size):
            if self.grid[x_index][column] == value:
                return True
        return False

    # Check if value already exists in 3x3 subgrid array constructed from current row/column values

    # Get sub 2D array range from passed in row/column coordinate

    def get_subarray_range(self, coord):
        if 0 <= coord <= 2:
            return 0, 3
        elif 2 < coord <= 5:
            return 3, 6
        else:
            return 6, 9

    # Get sub 2D array data (3x3 box) as a single list

    def get_subarray_data(self, row, column):
        subarray_data = []
        x_start, x_end = self.get_subarray_range(row)
        y_start, y_end = self.get_subarray_range(column)
        for x in range(x_start, x_end):
            for y in range(y_start, y_end):
                subarray_data.append(self.grid[x][y])
        return subarray_data

    # Check if num is already not in sub 2D array data (3x3 box)

    def value_in_subarray(self, value, row, column):
        current_subgrid = self.get_subarray_data(row, column)
        if value in current_subgrid:
            return True
        return False

    # 3-way check if a cell is a valid choice without conflicting without any constraints

    def cell_is_valid(self, value, row, column):
        if (
            not self.value_in_row(value, row)
            and not self.value_in_column(value, column)
            and not self.value_in_subarray(value, row, column)
        ):
            return True
        else:
            return False
