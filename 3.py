lines = []
with open('3-input.txt') as f:
    lines = f.readlines()
lines = [l[:-1] for l in lines]
print(lines)


priorities = {}
for i in range(26):
	priorities[chr(i+65)] = i + 27
	priorities[chr(i+97)] = i + 1


score = 0
for line in lines:
	a = set()
	b = set()
	for c in line[:len(line)/2]:
		a.add(c)
	for c in line[len(line)/2:]:
		b.add(c)

	score += priorities[list(a.intersection(b))[0]]

print(score)

