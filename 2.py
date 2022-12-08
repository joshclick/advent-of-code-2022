lines = []
with open('2-input.txt') as f:
    lines = f.readlines()
lines = [l[:-1] for l in lines]
print(lines)


me_score = {
	'X': 1,
	'Y': 2,
	'Z': 3,
}

score = 0
for line in lines:
	them, me = line.split()
	score += me_score[me]
	if ((them == 'A' and me == 'X') or
		(them == 'B' and me == 'Y') or
		(them == 'C' and me == 'Z')):
		score += 3
	elif ((them == 'A' and me == 'Y') or
		(them == 'B' and me == 'Z') or
		(them == 'C' and me == 'X')):
		score += 6

print(score)

