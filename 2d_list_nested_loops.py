
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print("Part 1 - Pozitia in grid/matrice")
print(number_grid[2][0])
print("Part 2 - Nested loop")
for row in number_grid:
    for col in row:
        print(col)
