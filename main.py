from grid import Grid

test_grid = Grid(9)

print(test_grid)

test_grid.insert(3, 0, 1)
test_grid.insert(4, 0, 2)
test_grid.insert(8, 0, 3)
test_grid.insert(7, 0, 4)
test_grid.insert(2, 1, 2)
test_grid.insert(3, 1, 3)
test_grid.insert(4, 1, 4)
test_grid.insert(1, 1, 6)
test_grid.insert(5, 1, 7)
test_grid.insert(8, 1, 8)
test_grid.insert(1, 2, 0)
test_grid.insert(8, 2, 1)
test_grid.insert(2, 2, 3)
test_grid.insert(9, 3, 0)
test_grid.insert(3, 3, 4)
test_grid.insert(5, 3, 6)
test_grid.insert(6, 3, 8)
test_grid.insert(1, 4, 1)
test_grid.insert(4, 4, 6)
test_grid.insert(5, 5, 1)
test_grid.insert(3, 5, 2)
test_grid.insert(7, 5, 3)
test_grid.insert(6, 5, 4)
test_grid.insert(2, 5, 8)
test_grid.insert(2, 6, 1)
test_grid.insert(6, 6, 3)
test_grid.insert(3, 6, 5)
test_grid.insert(7, 7, 0)
test_grid.insert(8, 7, 2)
test_grid.insert(5, 7, 5)
test_grid.insert(3, 7, 8)
test_grid.insert(3, 8, 0)
test_grid.insert(1, 8, 2)
test_grid.insert(4, 8, 3)
test_grid.insert(7, 8, 5)
test_grid.insert(8, 8, 6)
test_grid.insert(6, 8, 7)
test_grid.insert(5, 8, 8)


print(test_grid)


def find_solution(grid):
    # Base case, grid is full of valid non-conflicting values, starts propagating True trough call stack
    if grid.grid_is_full():
        print(grid)
        return True
    # Get next empty cell location from grid
    next_empty_cell_x, next_empty_cell_y = grid.get_empty_cell_coordinates()
    #   Start looping trough all valid values 1-9
    for num in range(1, grid.get_size() + 1):
        # print(num)
        # Check if num in loop step is valid for current empty cell
        if grid.cell_is_valid(num, next_empty_cell_x, next_empty_cell_y):
            # Insert valid num in to cell
            grid.insert(num, next_empty_cell_x, next_empty_cell_y)
            # Recursively call function on grid with inserted valid num in a free cell
            if find_solution(grid):
                # True propagates backwards trough the call queue from a filled in grid trough all call stacks (correct cell assignments)
                return True
            else:
                # if function cant find a grid_is_full == True with this version of grid with num inserted,
                # resets grid cell with 0 and continues down to return False! backtracking 1 stack back
                grid.insert(0, next_empty_cell_x, next_empty_cell_y)

    print("No valid solution exists for this branch of Sudoku")
    return False


find_solution(test_grid)
