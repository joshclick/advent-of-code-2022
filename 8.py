lines = []
with open('8-input') as f:
    lines = f.readlines()
lines = [l[:-1] for l in lines]


rows = len(lines)
cols = len(lines[0])

grid = []
visible = []
for line in lines:
	grid.append([int(c) for c in line])
	visible.append([0 for c in line])

print(grid)


for i in range(len(grid)):
	visible[i][0] = 1
	visible[i][len(grid) - 1] = 1

for j in range(len(grid[0])):
	visible[0][j] = 1
	visible[len(grid[0] - 1)][j] = 1


# left to right
for i in range(len(grid)):
	tallest = 0
	for j in range(len(grid[i])):
		if grid[i][j] > tallest:
			visible[i][j] = 1
			tallest = grid[i][j]

# right to left
for i in range(len(grid)):
	tallest = 0
	for j in range(len(grid[i])-1, -1, -1):
		if grid[i][j] > tallest:
			visible[i][j] = 1
			tallest = grid[i][j]

# top to bot
for i in range(len(grid)):
	tallest = 0
	for j in range(len(grid[i])):
		if grid[j][i] > tallest:
			visible[j][i] = 1
			tallest = grid[j][i]

# bot to top
for i in range(len(grid)):
	tallest = 0
	for j in range(len(grid[i])-1, -1, -1):
		if grid[j][i] > tallest:
			visible[j][i] = 1
			tallest = grid[j][i]


visible_sum = 0
for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j]:
			visible_sum += 1
print(visible_sum)
