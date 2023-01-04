from grid import Grid

test_grid = Grid(9)

# print(test_grid)

test_grid.insert(9, 1, 1)
test_grid.insert(2, 1, 2)
test_grid.insert(8, 0, 0)
test_grid.insert(5, 7, 8)
test_grid.insert(3, 0, 8)

print(test_grid)

print(test_grid.value_in_subarray(8, 0, 0))
print(test_grid.value_in_subarray(8, 5, 0))
print(test_grid.value_in_subarray(5, 8, 7))

print(test_grid.cell_is_valid(5, 6, 7))
