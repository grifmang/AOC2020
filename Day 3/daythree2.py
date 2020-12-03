result = []
with open('daythree.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        result.append(line.rstrip('\n').strip())

def through_grid(grid, right, down):
    x = y = 0
    count = 0
    while y < len(grid):
        if grid[y][x] == '#': count += 1
        y += down
        x = (x + right) % len(grid[0])

    return count

def find_trees(grid):
    count = []
    spots = [[1, 1], [3, 1], [5, 1] , [7, 1], [1, 2]]
    for spot in spots:
        count.append(through_grid(grid, spot[0], spot[1]))
    return count

count = find_trees(result)
counter = 1
for num in count:
    if num == 0: continue
    counter *= num

print(counter)