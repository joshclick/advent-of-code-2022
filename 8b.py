lines = []
with open('8-input') as f:
    lines = f.readlines()
lines = [l[:-1] for l in lines]


rows = len(lines)
cols = len(lines[0])

grid = []
scenic_score = []
for line in lines:
	grid.append([int(c) for c in line])
	scenic_score.append([0 for c in line])

print(grid)


for i in range(len(grid)):
	for j in range(len(grid[0])):
		curr_height = grid[i][j]
		# for every item, go up, down left and right
		up_score = 0
		for y in range(j-1, -1, -1):
			if grid[i][y] < curr_height:
				up_score += 1
			else:
				up_score += 1
				break

		down_score = 0
		for y in range(j+1, len(grid[0])):
			if grid[i][y] < curr_height:
				down_score += 1
			else:
				down_score += 1
				break

		left_score = 0
		for x in range(i-1, -1, -1):
			if grid[x][j] < curr_height:
				left_score += 1
			else:
				left_score += 1
				break

		right_score = 0
		for x in range(i+1, len(grid)):
			if grid[x][j] < curr_height:
				right_score += 1
			else:
				right_score += 1
				break
		scenic_score[i][j] = up_score * down_score * left_score * right_score



max_score = 0
for i in range(len(grid)):
	for j in range(len(grid[0])):
		if scenic_score[i][j] > max_score:
			max_score = scenic_score[i][j]
print(max_score)
