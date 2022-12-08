lines = []
with open('2-input.txt') as f:
    lines = f.readlines()
lines = [l[:-1] for l in lines]
print(lines)


shape_score = {
	'A': 1,
	'B': 2,
	'C': 3,
}

shapes = ['A', 'B', 'C']

score = 0
for line in lines:
	them, me = line.split()
	if me == 'X':
		score += 0
		score += shape_score[shapes[shape_score[them] - 2 % 3]]
	elif me == 'Y':
		score += 3
		score += shape_score[them]
	else:
		score += 6
		score += shape_score[shapes[shape_score[them] % 3]]

print(score)

