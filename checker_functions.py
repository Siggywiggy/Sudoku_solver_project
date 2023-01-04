def not_in_row(grid, value, row):
    if value in grid[row]:
        return False
    return True


def not_in_column(grid, value, column):

    column_values = [grid[row][column] for row in range(9) if grid[row][column] != 0]

    if value in column_values:
        return False
    return True


def not_in_subgrid(grid, value, row, column):
    current_subgrid = get_subgrid_data(grid, row, column)
    if value in current_subgrid:
        return False
    return True


def get_subgrid_range(coord):
    if 0 < coord <= 2:
        return 0, 3
    elif 2 < coord <= 5:
        return 3, 6
    else:
        return 6, 9


def get_subgrid_data(grid, row, column):
    cell_data = []
    x_start, x_end = get_subgrid_range(row)
    y_start, y_end = get_subgrid_range(column)
    for x in range(x_start, x_end):
        for y in range(y_start, y_end):
            cell_data.append(grid[x][y])
    return cell_data


